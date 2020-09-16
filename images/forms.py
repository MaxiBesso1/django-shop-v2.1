from django import forms
from .models import Images

class Form_Image(forms.ModelForm):
    class Meta:
        model = Images
        fields = ["name","image"]
        labels = {"name":"","image":""}
        widgets = {"name":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Image name","id":"id_name"}),
        "image":forms.FileInput(attrs={"class":"form-control my-2","placeholder":"Image","id":"id_image"})}