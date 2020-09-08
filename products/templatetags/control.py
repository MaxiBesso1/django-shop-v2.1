from django import template
from products_catalog.settings import FILE_TXT

register = template.Library()
@register.simple_tag
def get_categorys():
    with open(FILE_TXT,"r") as f:
        categorys = []
        characters = ""
        categorys_str = f.read()
        for x in categorys_str:
            if x != ",":
                characters += x
            else:
                categorys.append(characters)
                characters = ""
    return categorys


def get_categorys_as_tuple():
    categorys = []
    characters = ""
    with open(FILE_TXT,"r") as f:
        categorys_str = f.read()
        for x in categorys_str:
            if x != ",":
                characters += x
            else:
                tuple = (characters,characters)
                categorys.append(tuple)
                characters = ""
    return categorys

def get_categorys_as_str():
    with open(FILE_TXT,"r") as f:
        characters = ""
        categorys_str = f.read()
        for x in categorys_str:
            characters += x
    return characters

def add_category(category):
    categorys = get_categorys_as_str()
    with open(FILE_TXT,"w") as f:
        category1 = category + ","
        f.write(categorys + category1)

def edit_category(category,old):
    print("CALL IN EDIT",old,"to",category)
    categorys = get_categorys_as_str()
    characters = ""
    new = []
    for x in categorys:
        if x != ",":
                characters += x
        else:
            if characters == old:
                print("ENCONTRADO")
                characters = category 
            new.append(characters + ",")
            characters = ""  
    print(new)
    for x in new:
        for y in x:
            characters += y

    with open(FILE_TXT,"w") as f:
        f.write(characters)

def delete_category(old):
    categorys = get_categorys_as_str()
    characters = ""
    new = []
    for x in categorys:
        if x != ",":
                characters += x
        else:
            if characters != old:
                new.append(characters + ",")
            characters = ""  
    for x in new:
        for y in x:
            characters += y

    with open(FILE_TXT,"w") as f:
        f.write(characters)
               

            






    
