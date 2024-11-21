from django import forms
from .models import AuthUser
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from django import forms
from django.contrib.auth import authenticate
from django import forms 
from .models import AuthUser, Usuarios, Carrito
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Opciones para el campo "Género"
GENDER_CHOICES = (
    ('M', 'Masculino'),
    ('F', 'Femenino'),
    ('O', 'Otro'),
)

class CustomUserCreationForm(UserCreationForm):
    # Campos adicionales para el formulario
    email = forms.EmailField(required=True, label="Correo Electrónico")
    email2 = forms.EmailField(required=True, label="Confirmar Correo Electrónico")
    birth_date = forms.DateField(
        required=True, 
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Fecha de Nacimiento"
    )
    phone_number = forms.CharField(required=True, label="Número de Teléfono")
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True, label="Género")

    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'email', 'email2',
            'birth_date', 'phone_number', 'gender', 'password1', 'password2'
        )
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'email2': forms.EmailInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_username(self):
        """Validar que el nombre de usuario sea único."""
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError("Este nombre de usuario ya está en uso. Por favor, elige otro.")
        return username

    def clean_email(self):
        """Validar que el correo electrónico sea único."""
        email = self.cleaned_data.get('email')
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("Este correo electrónico ya está registrado. Por favor, utiliza otro.")
        return email

    def clean(self):
        """Validar que los correos electrónicos coincidan."""
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        email2 = cleaned_data.get('email2')

        if email and email2 and email != email2:
            self.add_error('email2', "Los correos electrónicos no coinciden.")
        return cleaned_data




from django import forms
from .models import AuthUser

class CustomLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su nombre de usuario'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su contraseña'}))


    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError("Credenciales inválidas. Por favor intente nuevamente.")


from django import forms
from django.contrib.auth.models import User

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']





from django import forms
from .models import Direccion

class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = ['region', 'comuna', 'destinatario', 'calle', 'numero', 'datos_adicionales']



from django import forms
from .models import AuthUser

class ActualizarPerfilForm(forms.ModelForm):
    class Meta:
        model = AuthUser
        fields = ['birth_date', 'phone_number', 'gender']  # Solo los campos que se necesitan
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }


from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    imagen = forms.ImageField(required=False)  # Campo para subir la imagen

    class Meta:
        model = Libro
        fields = ['isbn', 'titulo', 'autor', 'categoria', 'descripcion', 'precio', 
                  'stock', 'formato', 'idioma', 'anio', 'num_paginas', 'encuadernacion', 
                  'dimensiones', 'imagen']  # Incluye el campo de imagen
        
from django import forms
from .models import LVentaU, Autor, Categoria

class LVentaUForm(forms.ModelForm):
    tipo_registro = forms.ChoiceField(
        choices=[('venta', 'Venta'), ('intercambio', 'Intercambio')],
        widget=forms.RadioSelect(attrs={'onchange': 'togglePrecioInput(this.value)'})
    )
    
    class Meta:
        model = LVentaU
        fields = ['isbn', 'titulo', 'autor', 'categoria', 'precio', 'stock', 'estado', 'descripcion', 'tipo_registro', 'imagen_url']
        widgets = {
            'precio': forms.NumberInput(attrs={'step': '0.01'}),
            'descripcion': forms.Textarea(attrs={'rows': 3}),
            'imagen_url': forms.FileInput(attrs={'accept': 'image/*'}),
        }
        labels = {
            'isbn': 'ISBN',
            'titulo': 'Título del Libro',
            'autor': 'Autor',
            'categoria': 'Categoría',
            'precio': 'Precio (CLP)',
            'stock': 'Stock',
            'estado': 'Estado',
            'descripcion': 'Descripción',
            'imagen_url': 'Imagen',
        }

    def clean_precio(self):
        tipo_registro = self.cleaned_data.get('tipo_registro')
        precio = self.cleaned_data.get('precio')
        if tipo_registro == 'venta' and (precio is None or precio <= 0):
            raise forms.ValidationError('El precio es obligatorio para el registro de tipo venta.')
        elif tipo_registro == 'intercambio':
            return 0  # Si es intercambio, devolver 0 como precio
        return precio
from django import forms
from .models import Solicitudintercambio

class SeleccionarLibroForm(forms.ModelForm):
    class Meta:
        model = Solicitudintercambio
        fields = ['libro_intercambio']
        labels = {'libro_intercambio': 'Selecciona un libro del catálogo del solicitante'}




from django import forms
from django.core.exceptions import ValidationError
from .models import LVentaU, Libro, AuthUser

class LVentaUForm(forms.ModelForm):
    class Meta:
        model = LVentaU
        fields = ['isbn', 'titulo', 'autor', 'categoria', 'precio', 'stock', 'estado', 
                  'descripcion', 'solicitud', 'usuario', 'tipo_registro', 'imagen_url']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'imagen_url': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio is not None and precio <= 0:
            raise ValidationError('El precio debe ser mayor que 0.')
        return precio

    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock is not None and stock < 0:
            raise ValidationError('El stock no puede ser negativo.')
        return stock

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['isbn', 'titulo', 'autor', 'categoria', 'descripcion', 'precio', 
                  'stock', 'formato', 'idioma', 'anio', 'num_paginas', 
                  'encuadernacion', 'dimensiones', 'imagen_url']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'imagen_url': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio is not None and precio <= 0:
            raise ValidationError('El precio debe ser mayor que 0.')
        return precio

    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock is not None and stock < 0:
            raise ValidationError('El stock no puede ser negativo.')
        return stock

class AuthUserForm(forms.ModelForm):
    class Meta:
        model = AuthUser
        fields = ['username', 'email', 'first_name', 'last_name', 
                  'is_staff', 'is_active', 'birth_date', 'phone_number', 'gender']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(choices=[
                ('', 'Seleccione'),
                ('Masculino', 'Masculino'),
                ('Femenino', 'Femenino'),
                ('Otro', 'Otro')
            ], attrs={'class': 'form-control'}),
            'is_staff': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
