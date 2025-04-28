from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeDoneView


# Vista de registro de usuario
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            messages.success(request, '¡Te registraste exitosamente!')
            return redirect('home') 
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

# Vista de perfil
@login_required
def profile_view(request):
    user = request.user
    profile = user.profile
    return render(request, 'accounts/profile.html', {
        'user': user,
        'profile': profile,
    })

# Vista de Edición de perfil    
@login_required
def profile_edit(request):
    profile = request.user.profile  # accedemos al perfil del usuario logueado

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Perfil actualizado exitosamente!')
            return redirect('profile')  # te redirige al perfil actualizado
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'accounts/profile_edit.html', {'form': form})

# Edición de Contraseña
class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/password_change.html'
    def form_valid(self, form):
        messages.success(self.request, '¡Tu contraseña fue cambiada exitosamente!')
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('profile') 

class CustomPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'accounts/password_change_done.html'

# Vista de logout
def logout_view(request):
    logout(request)
    return redirect('home')

# Vista de login
class CustomLoginView(LoginView):
    template_name = "accounts/login.html"
  
  


