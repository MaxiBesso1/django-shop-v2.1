from django.urls import path
from products import views as v
from django.shortcuts import HttpResponseRedirect
urlpatterns = [
    path("inicio/",v.Index.as_view(),name="index"),
    path("productos/<int:pk>/",v.A_product.as_view()),
    path("c/<str:category>/",v.All_product.as_view()),
]