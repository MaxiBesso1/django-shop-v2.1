from random import sample
from django.shortcuts import render,HttpResponseRedirect
from django.views.generic import UpdateView,CreateView,ListView,DeleteView,TemplateView,View
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from .models import Product
from styles.models import Banner1 as Banner
from .templatetags.control import get_categorys

class Index(View):
    template_name = "products/index.html"
    models = [Product,Banner]
    def get(self,request,*args,**kwargs):
        styles = self.models[1].objects.get(id=1)
        products = sample(list(self.models[0].objects.filter(offer=False)),1)
        products_offer = self.models[0].objects.filter(offer=True)
        context = {"bann":styles,"products":products,"offers":products_offer}
        return render(request,self.template_name,context)

class A_product(View):
    template_name = "products/product.html"
    model = Product
    def get(self,request,pk,*args,**kwargs):
        return render(request,self.template_name,{"p":self.model.objects.get(id=pk),"products":sample(list(self.model.objects.all()),2)})

class All_product(View):
    template_name = "products/all.html"
    model = Product
    extra_data = get_categorys()
    def get(self,request,category,*args,**kwargs):
        res = False
        for x in self.extra_data:
            if x == category:
                res=True
        if res:
            products= self.model.objects.filter(category=category)
            paginator = Paginator(products, per_page=3)
            page_number = request.GET.get('page', 1)
            page_obj = paginator.get_page(page_number)
            context = {"products":products,'paginator': paginator,'page_number': int(page_number),"category":category}

        elif category == "all":
            products= self.model.objects.all()
            paginator = Paginator(products, per_page=3)
            page_number = request.GET.get('page', 1)
            page_obj = paginator.get_page(page_number)
            context = {"products":products,'paginator': paginator,'page_number': int(page_number),"category":"Nuestros productos"}
        else:
            context = {"products":False}
        return render(request,self.template_name,context)



    


