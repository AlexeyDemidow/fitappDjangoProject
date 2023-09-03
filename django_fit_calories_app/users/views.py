from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm, CustomUserChangeForm, WeighingForm
from .models import CustomUser, Weighing
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required


# Представление страницы регистрации
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('signup_success')
    template_name = 'signup.html'


# Представление страницы после успешной регистрации
def signup_success(request):
    return render(request, 'signup_success.html')


# Представление страницы профиля
@login_required
def profile(request, username):
    user = get_object_or_404(CustomUser, username=username)
    userweight = Weighing.objects.filter(user=user.id)

    data_weight = [user.weight]
    date_labels = [user.date_joined.strftime("%d-%m-%Y")]

    for weight in userweight:
        if weight.weighing_date.strftime("%d-%m-%Y") not in date_labels:
            data_weight.append(weight.weight_value)
            date_labels.append(weight.weighing_date.strftime("%d-%m-%Y"))
        else:
            date_labels[-1] = weight.weighing_date.strftime("%d-%m-%Y")
            data_weight[-1] = weight.weight_value

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


# Представление страницы редактирования профиля
@login_required
def edit_profile(request, username):
    user = get_object_or_404(CustomUser, username=username)

    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('charts')
    else:
        form = CustomUserChangeForm(instance=user)

    birth_date = str(user.birth_date)

    context = {
        'form': form,
        'birth_date': birth_date,
    }
    return render(request, 'edit_profile.html', context)
