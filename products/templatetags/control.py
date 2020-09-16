from django import template

register = template.Library()
@register.simple_tag
def get_categorys():
    try:
        from products.models import Category
        categorys = Category.objects.all()
        categorys_list = []
        for x in categorys:
            categorys_list.append(x.name)
        return categorys_list
    except:
        return ["categoria 1","categoria 2","categoria 3"]




            






    
