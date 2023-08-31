# Create your views here.
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CustomUser, Weighing
from .forms import CustomUserChangeForm, WeighingForm
from django.shortcuts import redirect
import datetime



class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


@login_required
def profile(request, username):
    user = get_object_or_404(CustomUser, username=username)
    userweight = Weighing.objects.filter(user=user.id)

    data_weight = [user.weight]
    date_labels = [user.date_joined.strftime("%d-%m-%Y")]
    for i in userweight:
        if i.weighing_date.strftime("%d-%m-%Y") not in date_labels:
            data_weight.append(i.weight_value)
            date_labels.append(i.weighing_date.strftime("%d-%m-%Y"))
        else:
            date_labels[-1] = i.weighing_date.strftime("%d-%m-%Y")
            data_weight[-1] = i.weight_value

    if len(data_weight) > 0:
        user.weight = data_weight[-1]

    if request.method == "POST":
        form = WeighingForm(request.POST, initial={'user': user})
        if form.is_valid():
            form.save()
            return redirect('profile', username=request.user.username)
    else:
        form = WeighingForm(initial={'user': user})

    context = {
        'user': user,
        'form': form,
        'date_labels': date_labels,
        'data_weight': data_weight,
    }
    return render(request, 'profile.html', context)


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


