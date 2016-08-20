from django import forms

class RegisterForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.CharField(label='Email', max_length=50)
    password = forms.CharField(label='Password', min_length=4)
    passwordConfirm = forms.CharField(label='Password Confirm', min_length=4)

class ProfileForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.CharField(label='Email', max_length=50)
    doc = forms.IntegerField(label='Doc')
    telefono = forms.CharField(label='Doc', max_length=15)
    direccion = forms.CharField(label='Doc', max_length=15)

class PasswordForm(forms.Form):
    password = forms.CharField(label='Password', min_length=4)
    passwordConfirm = forms.CharField(label='Password Confirm', min_length=4)

class ContactoForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    apellido = forms.CharField(label='Apellido', max_length=100)
    direccion = forms.CharField(label='Direccion', max_length=100)
    telefono = forms.CharField(label='Telefono', max_length=100)
    email = forms.CharField(label='Email', max_length=100)
    apodo = forms.CharField(label='Apodo', max_length=100)

class AvatarImageForm(forms.Form):
    image = forms.ImageField()