from django import forms

from .models import Banner1
class Banner_form(forms.ModelForm):
    class Meta:
        model = Banner1
        fields = ["banner","banner_2","banner_3","title","title_color","title_2","title_color_2","title_3",
        "title_color_3","subtitle","subtitle_color","subtitle_2","subtitle_color_2","subtitle_3","subtitle_color_3",
        "status","status_2","status_3","login_image"]
        labels = {"banner":"Imagenes","banner_2":"","banner_3":"",
        "title":"Titulos","title_color":"","title_2":"","title_color_2":"","title_3":"","title_color_3":"",
        "subtitle":"Subtitulos","subtitle_color":"","subtitle_2":"","subtitle_color_2":"","subtitle_3":"","subtitle_color_3":"",
        "status":"Estado general","status_2":"Imagen 2","status_3":"Imagen 3","login_image":"Imagen del inicio de sesion"}

        widgets = {"title":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Titulo del banner"}),
            "title_color":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Color del titulo (CODIGO CON #)"}),
            "title_2":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Titulo del banner 2"}),
            "title_color_2":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Color del titulo 2 (CODIGO CON #)"}),
            "title_3":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Titulo del banner 3"}),
            "title_color_3":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Color del titulo 3(CODIGO CON #)"}),
            "subtitle":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Subtitulo del banner"}),
            "subtitle_color":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Color del subtitulo (CODIGO CON #)"}),
            "subtitle_2":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Subtitulo del banner 2"}),
            "subtitle_color_2":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Color del subtitulo 2 (CODIGO CON #)"}),
            "subtitle_3":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Subtitulo del banner 3"}),
            "subtitle_color_3":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Color del subtitulo 3 (CODIGO CON #)"}),
            "banner":forms.Select(attrs={"class":"form-control my-1","placeholder":"Imagen del banner (GRANDE)"}),
            "banner_2":forms.Select(attrs={"class":"form-control my-1","placeholder":"Imagen del banner 2 (GRANDE)"}),
            "banner_3":forms.Select(attrs={"class":"form-control my-1","placeholder":"Imagen del banner 3 (GRANDE)"}),
            "status":forms.CheckboxInput(attrs={"class":"form-control my-1"}),
            "status_2":forms.CheckboxInput(attrs={"class":"form-control my-1"}),
            "status_3":forms.CheckboxInput(attrs={"class":"form-control my-1"}),
            "login_image":forms.Select(attrs={"class":"form-control my-1","placeholder":"Imagen del inicio de sesion"})}