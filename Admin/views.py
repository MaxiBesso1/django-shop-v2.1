from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import UpdateView,DeleteView,View,ListView,CreateView
from products.models import Product
from styles.models import Banner1 as Banner
from products.forms import Product_form
from styles.forms import Banner_form 
from .mixins import SuperUserMixin,AjaxMixin
from products.templatetags.control import add_category,get_categorys,edit_category,delete_category
# Create your views here.

class Admin(SuperUserMixin,View):
    template_name = "admin/admin_index.html"
    models = [Product,Banner]
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
            context["objects"] = get_categorys()
            context["name"] = "Categorias"

        return context

#Add admin mixin
class New_product(SuperUserMixin,CreateView):
    template_name = "admin/form.html"
    model = Product
    form_class = Product_form
    success_url = reverse_lazy("admin",args=("productos",))

class Edit_product(SuperUserMixin,AjaxMixin,UpdateView):
    template_name = "admin/modal.html"
    model = Product
    form_class = Product_form
    success_url = reverse_lazy("admin",args=("productos",))   
     

class Delete_product(SuperUserMixin,DeleteView):
    model = Product
    success_url = reverse_lazy("admin",args=("productos",))

class Edit_styles(SuperUserMixin,AjaxMixin,UpdateView):
    template_name = "admin/modal.html"
    model = Banner
    form_class = Banner_form
    success_url = reverse_lazy("admin",args=("estilos",))  

class New_category(SuperUserMixin,View):
    template_name = "admin/form_c.html"
    def get(self,request,*args,**kwargs):
        return render(request,self.template_name)
    def post(self,request,*args,**kwargs):
        add_category(request.POST["category"])
        return HttpResponseRedirect("/admin/categorias")

class Edit_category(SuperUserMixin,AjaxMixin,View):
    template_name = "admin/modal1.html"
    category_old = ""
    def get(self,request,category,*args,**kwargs):
        self.category_old = category
        return render(request,self.template_name,{"old_category":self.category_old})
    def post(self,request,category,*args,**kwargs):
        edit_category(request.POST["category"],category)
        return HttpResponseRedirect("/admin/categorias")

class Delete_category(SuperUserMixin,View):
    template_name = "admin/modal2.html"
    category_old = ""
    def get(self,request,category,*args,**kwargs):
        self.category_old = category
        return render(request,self.template_name,{"old_category":self.category_old})
    def post(self,request,category,*args,**kwargs):
        delete_category(category)
        return HttpResponseRedirect("/admin/categorias")   

