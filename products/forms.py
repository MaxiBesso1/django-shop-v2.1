from django import forms
from .models import Product,Category
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User




class Product_form(forms.ModelForm):      
    class Meta:
        model = Product
        fields = ["name","price","description","category","principal_image","banner_images","offer","new_price"]
        labels = {"name":"","price":"","description":"","category":"","principal_image":"","banner_images":"","offer":"Oferta","new_price":""}
        widgets = {"name":forms.TextInput(attrs={"class":"form-control m-1","placeholder":"Nombre"})
        ,"price":forms.NumberInput(attrs={"class":"form-control m-1","placeholder":"Precio"})
        ,"description":forms.Textarea(attrs={"class":"form-control m-1","placeholder":"Descripcion"})
        ,"category": forms.Select(attrs={"class":"form-control m-1","placeholder":"Categoria"})
        ,"principal_image":forms.Select(attrs={"class":"form-control m-1","placeholder":"Imagen de cabecera"})
        ,"banner_images":forms.SelectMultiple(attrs={"class":"form-control m-1","placeholder":"Imagenes del producto"})
        ,"offer":forms.CheckboxInput(attrs={"class":"form-check-input m-1"})
        ,"new_price":forms.NumberInput(attrs={"class":"form-control m-1","placeholder":"Precio de oferta"})} 
   


#Edit the login form for more pleasure
class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields["username"].label=""
        self.fields["password"].label=""
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control my-2', 'placeholder': 'Nombre de usuario'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control my-2','placeholder': 'Contraseña',}))   

class Form_category(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]
        labels = {"name":""}
        widgets = {"name":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Category name"})}


     
        
