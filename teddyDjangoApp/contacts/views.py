# -*- coding: utf-8 -*-

import ast
import json
import pprint
from teddyDjangoApp import settings
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, UpdateView, CreateView, DeleteView
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.template.defaulttags import register
from django.forms.models import model_to_dict

from django.db.models import Min, Max, Sum
from django.core.serializers.json import DjangoJSONEncoder
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


from contacts.models import UserProfile, Contacto, Detalle
from contacts.forms import RegisterForm, ContactoForm, ProfileForm, PasswordForm
from django.shortcuts import render_to_response
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .forms import AvatarImageForm

# from django.template import Library, Node, Variable, TemplateSyntaxError
# register = Library()

# Create your views here.
def loginUser(request):

	next = request.GET.get('next', '/')
	errorMessage = ''

	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		
		pprint.pprint("hace")
		if user is not None:

			pprint.pprint("login ok")

			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(next)
			else:
				return HttpResponse("Inactive user.")
		else:

			pprint.pprint("login malo")
			# return HttpResponseRedirect(settings.LOGIN_URL)
			errorMessage = 'Usuario o contrasenha incorrectos'

	pprint.pprint("carga")
	return render(request, "login.html", {'redirect_to': next, 'error' : errorMessage})


def logoutUser(request):
    context = {}
    try:
        auth_logout(request)
    except:
        pprint.pprint("Error on logout")

    return HttpResponseRedirect('/')


def home(request):
	return render(request, 'home.html')
    # if request.user.is_authenticated():
    #     return render(request, 'home.html')
    # else:
    #     return HttpResponseRedirect(reverse('auth_login'))

def registerUser(request):

	if request.method == "POST":
		theForm = RegisterForm(request.POST)

		# check whether it's valid:
		if theForm.is_valid():
			user = User.objects.create_user(theForm.cleaned_data['name'], theForm.cleaned_data['email'], theForm.cleaned_data['password'])

			profile = UserProfile()
			profile.user = user
			profile.telefono = '--'

			profile.save()

			return HttpResponseRedirect('/')

	else:
		theForm = RegisterForm()


	return render(request, 'register.html', {'form' : theForm})

@login_required
def perfilEdit(request):

	try:
		profile = UserProfile.objects.get(user_id=request.user.pk)
	except UserProfile.DoesNotExist:
		return HttpResponseRedirect('/')

	if request.method == "POST":
		theForm = ProfileForm(request.POST)

		# check whether it's valid:
		if theForm.is_valid():
			profile.name = theForm.cleaned_data['name']
			profile.email = theForm.cleaned_data['email']
			profile.doc = theForm.cleaned_data['doc']
			profile.telefono = theForm.cleaned_data['telefono']
			profile.direccion = theForm.cleaned_data['direccion']

			profile.save()

			messages.add_message(request, messages.SUCCESS, "Su perfil ha sido editado con exito")

			return HttpResponseRedirect('/')
	else:
		theForm = ProfileForm(model_to_dict(profile))


	return render(request, 'profile_form.html', {'form' : theForm})

@login_required
def avatarUpload(request):

	if request.method == "POST":
		theForm = AvatarImageForm(request.POST)

		# check whether it's valid:
		if theForm.is_valid():
			m = UserProfile.objects.get(user_id=request.user.pk)
			m.avatar = form.cleaned_data['image']
			m.save()
			# user = User.objects.get(pk=request.user.pk)
			# user = User.objects.create_user(theForm.cleaned_data['name'], theForm.cleaned_data['email'], theForm.cleaned_data['password'])

			# profile = UserProfile()
			# profile.user = user
			# profile.telefono = '--'

			# profile.save()

			return HttpResponseRedirect('/avatar')

	else:
		theForm = ProfileForm()


	return render(request, 'profile_form.html', {'form' : theForm})

@login_required
def passwordEdit(request):

	if request.method == "POST":
		theForm = PasswordForm(request.POST)

		# check whether it's valid:
		if theForm.is_valid():
			user = User.objects.get(pk=request.user.pk)

			user.set_password(theForm.cleaned_data['password'])
			user.save()

			return HttpResponseRedirect('/')

	else:
		theForm = PasswordForm()


	return render(request, 'password_form.html', {'form' : theForm})

@login_required
def contactoList(request):

	contactos = Contacto.objects.all()

	return render(request, 'contact_list.html', {'contactos' : contactos})

@login_required
def contactoEdit(request, id_contacto):

	try:
		contacto = Contacto.objects.get(pk=id_contacto)
	except Contacto.DoesNotExist:
		return HttpResponseRedirect('contactoList')

	if request.method == "POST":
		theForm = ContactoForm(request.POST)

		# check whether it's valid:
		if theForm.is_valid():
			contacto.nombre = theForm.cleaned_data['nombre']
			contacto.apellido = theForm.cleaned_data['apellido']
			contacto.apodo = theForm.cleaned_data['apodo']
			contacto.telefono = theForm.cleaned_data['telefono']
			contacto.email = theForm.cleaned_data['email']
			contacto.direccion = theForm.cleaned_data['direccion']

			contacto.save()

			messages.add_message(request, messages.SUCCESS, "Su contacto ha sido editado con exito")

			return HttpResponseRedirect('/contact/list')
	else:
		theForm = ContactoForm(model_to_dict(contacto))


	return render(request, 'contact_form.html', {'form' : theForm})

@login_required
def contactoDelete(request, id_contacto):
	return render(request, 'contact_form.html', {'form' : theForm})

@login_required
def contactoAdd(request):

	if request.method == "POST":
		theForm = ContactoForm(request.POST)

		# check whether it's valid:
		if theForm.is_valid():
			c = Contacto()
			c.nombre = theForm.cleaned_data['nombre']
			c.apellido = theForm.cleaned_data['apellido']
			c.apodo = theForm.cleaned_data['apodo']
			c.telefono = theForm.cleaned_data['telefono']
			c.email = theForm.cleaned_data['email']
			c.direccion = theForm.cleaned_data['direccion']

			c.save()

			# messages.add_message(request, level, message, extra_tags='', fail_silently=False)
			# https://docs.djangoproject.com/en/1.9/ref/contrib/messages/
			# DEBUG	Development-related messages that will be ignored (or removed) in a production deployment
			# INFO	Informational messages for the user
			# SUCCESS	An action was successful, e.g. “Your profile was updated successfully”
			# WARNING	A failure did not occur but may be imminent
			# ERROR	An action was not successful or some other failure occurred

			messages.add_message(request, messages.SUCCESS, "Su contacto ha sido guardado con exito")

			return HttpResponseRedirect('/contact/list')

	else:
		theForm = ContactoForm()


	return render(request, 'contact_form.html', {'form' : theForm})


@register.filter(name='addclass')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg})
