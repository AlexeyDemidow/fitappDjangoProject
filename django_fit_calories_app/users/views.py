# Create your views here.
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CustomUser, Weighing
from .forms import CustomUserChangeForm
from django.shortcuts import redirect



class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


@login_required
def profile(request, username):
    user = get_object_or_404(CustomUser, username=username)
    return render(request, 'profile.html', {'user': user})


@login_required
def edit_profile(request, username):
    user = get_object_or_404(CustomUser, username=username)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile', username=request.user.username)
    else:
        form = CustomUserChangeForm(instance=user)
    return render(request, 'edit_profile.html', {'form': form})

@login_required
def weighing(request, username):
    user = get_object_or_404(CustomUser, username=username)
    userw = Weighing.objects.filter(user=user.id)
    q = []
    for i in userw:
        q.append(i.weight_value)
    if len(q) > 0:
        user.weight = q[0]
    print(user.weight)
    context = {'user': user}
    return render(request, 'profile.html', context)