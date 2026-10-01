from django import forms
from .models import ArchivoSubido

class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length=80, label="Nombre")
    correo = forms.EmailField(label="Correo electrónico")
    asunto = forms.CharField(max_length=120, label="Asunto")
    mensaje = forms.CharField(widget=forms.Textarea(attrs={"rows":5}), label="Mensaje")

class ArchivoForm(forms.ModelForm):
    class Meta:
        model = ArchivoSubido
        fields = ["nombre","archivo"]
