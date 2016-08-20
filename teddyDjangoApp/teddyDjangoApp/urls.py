"""observatorio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
# from contacts.views import (home, login, register)
from contacts import views as contactsViews

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # comentar las url para las vistas de registro que trae django auth
    # url(r'^accounts/profile/',  RedirectView.as_view(url='/', permanent=False)),
    # url(r'^accounts/', include('registration.backends.default.urls')),

    url(r'^$', contactsViews.home, name='home'),
    url(r'^register', contactsViews.registerUser, name='register'),

    url(r'^contact/add', contactsViews.contactoAdd, name='contactoAdd'),
    url(r'^contact/list', contactsViews.contactoList, name='contactoList'),
    url(r'^contact/edit/(?P<id_contacto>\d+)/', contactsViews.contactoEdit, name='contactoEdit'),
    url(r'^contact/delete/(?P<id_contacto>\d+)/', contactsViews.contactoDelete, name='contactoDelete'),
    
    url(r'^perfil/edit/', contactsViews.perfilEdit, name='perfilEdit'),
    url(r'^password/change/', contactsViews.passwordEdit, name='passwordEdit'),

    url(r'^login', contactsViews.loginUser),
    # url(r'^register', 'vialidad.views.registerUser'),
    url(r'^logout', contactsViews.logoutUser),
    # url(r'^about', views.about),
]
