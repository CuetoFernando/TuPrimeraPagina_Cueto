"""
URL configuration for TuPrimeraPagina_Cueto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.blog import views as blog_views
from apps.pages import views as pages_views
from apps.accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog_views.home, name='home'),
    path('about/', blog_views.about, name='about'),
    path('pages/', include('apps.pages.urls')),
    path('profile/', accounts_views.profile_view, name='profile'),
    path('logout/', accounts_views.logout_view, name='logout'),
    path('login/', accounts_views.CustomLoginView.as_view(), name='login'),
    path('signup/', accounts_views.signup, name='signup'),
    path('blog/', include('apps.blog.urls')),  # SOLO ESTA línea para blog
    path('accounts/', include('apps.accounts.urls')),
    path('messenger/', include('apps.messenger.urls')),
    path('como_funciona/', blog_views.como_funciona, name='como_funciona'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
