from django.urls import path 
from . import views as v
from django.contrib.auth.views import LoginView,LogoutView
from products.forms import UserLoginForm
from products.get_colores import get_image 

urls_admin = [
    path("admin/<str:part>",v.Admin.as_view(),name="admin"),
    path("nuevo/producto",v.New_product.as_view()),
    path("nueva/categoria",v.New_category.as_view()),
    path("editar/producto/<int:pk>",v.Edit_product.as_view()),
    path("editar/estilo/<int:pk>",v.Edit_styles.as_view()),
    path("editar/categoria/<str:category>",v.Edit_category.as_view()),
    path("borrar/producto/<int:pk>",v.Delete_product.as_view()),
    path("borrar/categoria/<str:category>",v.Delete_category.as_view()),
    path("accounts/profile/",LoginView.as_view(template_name="login.html",form_class=UserLoginForm,extra_context = {"image":get_image()}),name="login"),
    path("salir/",LogoutView.as_view()),


]