from django import forms
from .models import Product
from .templatetags.control import get_categorys_as_tuple
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User




class Product_form(forms.ModelForm):      
    CHOICES = get_categorys_as_tuple()
    category = forms.ChoiceField(choices=CHOICES,label="",widget=forms.Select(attrs={'class':'form-control m-1','placeholder':'Categorias',}))  
    class Meta:
        model = Product
        fields = ["name","price","description","category","link","principal_image","banner_image1","banner_image2","banner_image3","offer","new_price"]
        labels = {"name":"","price":"","description":"","category":"","link":"","principal_image":"","banner_image1":"","banner_image2":"","banner_image3":"","offer":"Oferta","new_price":""}
        widgets = {"name":forms.TextInput(attrs={"class":"form-control m-1","placeholder":"Nombre"})
        ,"price":forms.NumberInput(attrs={"class":"form-control m-1","placeholder":"Precio"})
        ,"description":forms.Textarea(attrs={"class":"form-control m-1","placeholder":"Descripcion"})
        ,"category": forms.Select(attrs={"class":"form-control m-1","placeholder":"Categoria"})
        ,"link":forms.TextInput(attrs={"class":"form-control m-1","placeholder":"Link de pago"})
        ,"principal_image":forms.FileInput(attrs={"class":"form-control m-1","placeholder":"Imagen de cabecera"})
        ,"banner_image1":forms.FileInput(attrs={"class":"form-control m-1","placeholder":"Imagen de producto 1"})
        ,"banner_image2":forms.FileInput(attrs={"class":"form-control m-1","placeholder":"Imagen de producto 2"})
        ,"banner_image3":forms.FileInput(attrs={"class":"form-control m-1","placeholder":"Imagen de producto 3"})
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


     
        
