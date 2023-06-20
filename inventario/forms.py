from django import forms

from .models import productos


class ProductosForm(forms.ModelForm):
    class Meta:
        model = productos
        fields = "__all__"
