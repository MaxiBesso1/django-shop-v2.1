from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import UpdateView,DeleteView,View,ListView,CreateView
from products.models import Product,Category
from styles.models import Banner1 as Banner
from products.forms import Product_form,Form_category
from styles.forms import Banner_form 
from .mixins import SuperUserMixin
from images.models import Images
from images.forms import Form_Image
from images.firebase import submit_to_firebase
# Create your views here.

class Admin(SuperUserMixin,View):
    template_name = "admin/admin_index.html"
    models = [Product,Banner,Category,Images]
    def get(self,request,part,*args,**kwargs):
        if User.is_staff:
            context = self.get_part(part)
            return render(request,self.template_name,context)
        else:
            return HttpResponseRedirect("/inicio/")

    def get_part(self,part):
        context = {}
        if part == "productos":
            context["objects"] = self.models[0].objects.all()
            context["name"] = "Productos"
        elif part == "estilos":
            context["objects"] = self.models[1].objects.all()
            context["name"] = "Estilos"
        elif part == "categorias":
            context["objects"] = self.models[2].objects.all()
            context["name"] = "Categorias"
        elif part == "imagenes":
            context["objects"] = self.models[3].objects.all()
            context["name"] = "Imagenes"

        return context

class New_product(SuperUserMixin,CreateView):
    template_name = "admin/form.html"
    model = Product
    form_class = Product_form
    success_url = reverse_lazy("admin",args=("productos",))

class Edit_product(SuperUserMixin,UpdateView):
    template_name = "admin/modal.html"
    model = Product
    form_class = Product_form
    success_url = reverse_lazy("admin",args=("productos",))   
     
class Delete_product(SuperUserMixin,DeleteView):
    model = Product
    success_url = reverse_lazy("admin",args=("productos",))

class Edit_styles(SuperUserMixin,UpdateView):
    template_name = "admin/modal3.html"
    model = Banner
    form_class = Banner_form
    success_url = reverse_lazy("admin",args=("estilos",))  

class New_category(SuperUserMixin,CreateView):
    template_name = "admin/form.html"
    model = Category
    form_class = Form_category
    success_url = reverse_lazy("admin",args=("categorias",))

class Edit_category(SuperUserMixin,View):
    template_name = "admin/modal3.html"
    model = Category
    form_class = Form_category
    success_url = reverse_lazy("admin",args=("categorias",)) 

class Delete_category(SuperUserMixin,View):
    template_name = "admin/modal2.html"
    success_url = reverse_lazy("admin",args=("categorias",))
    model = Category

class New_image(SuperUserMixin,CreateView):
    template_name = "admin/form.html"
    model = Images
    form_class = Form_Image
    def post(self,request,*args,**kwargs):
        name = request.POST.get("name")
        image = request.FILES.get("image")
        final_image,image2 = Images.objects.get_or_create(name=name,image=image)
        url_finaly = submit_to_firebase(final_image.image.url,name)
        final_image.url = url_finaly
        final_image.save()
        return HttpResponseRedirect("/admin/imagenes")

class Init_styles(SuperUserMixin,CreateView):
    template_name = "admin/form.html"
    model = Banner
    form_class = Banner_form
    success_url = reverse_lazy("admin",args=("estilos",))