from django import forms
from django.forms import ModelForm
from .models import Produto, Compra

#Formulário para Login de Usuário.
class LoginForm(forms.Form):
    usuario = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Usuário'}))
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}))

#Formulário para cadastro de Produto
class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['nome']




#Formulário para cadastro de Compra.
class CompraForm(ModelForm):
    class Meta:
        model = Compra
        #O formulário tem os campos produto, quantidade e preço, não tem o campo preço médio
        #pois é calculado pelo sistema.
        fields = ['produto', 'quantidade', 'preco_de_compra']
