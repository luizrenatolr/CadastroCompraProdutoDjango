from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('lista-compra/', views.listar_compras, name='lista_compra'),
    path('realizar-compra/', views.realizar_compra, name='realizar_compra'),
    path('logout/', views.logout_view, name='logout'),
    path('cadastrar-produto/', views.cadastrar_produto, name='cadastrar_produto'),
    path('', views.inicio, name='inicio')
]
