from django.shortcuts import render, redirect
from .forms import UserCreationForm
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
  return render(request, 'blog/base.html')

def register(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('login')
  else:
    form = UserCreationForm()
  context = {'form': form}
  return render(request, 'blog/register.html', context)

@login_required
def profile(request):
  if request.method == 'POST':
    user_form = UserUpdateForm(request.POST, instance = request.user)
    profile_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
    if user_form.is_valid() and ProfileUpdateForm.is_valid():
      user_form.save()
      profile_form.save()
  else:
    user_form = UserUpdateForm(instance = request.user)
    profile_form = ProfileUpdateForm(instance = request.user.profile)
  context = {"user_form": user_form, "profile_form": profile_form}
  return render(request, 'blog/profile', context)

