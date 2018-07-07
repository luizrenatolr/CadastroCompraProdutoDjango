from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .models import Produto, Compra
from .forms import ProdutoForm, CompraForm, LoginForm



#Função para fazer login.
def login_view(request):
    if request.method == "POST":
        #Se o método de requisição for POST, há dados de formulario para serem recebidos.
        form = LoginForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            senha = form.cleaned_data['senha']
            user = authenticate(username = usuario, password = senha)
            if user is not None:
                #Se os dados de login e senha estão corretos, fazer login e redirecionar para página inicial.
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                #Se os dados não estão corretos retornar mensagem de erro e
                # redirecionar para página de login navamente com um novo formulário.
                erro = "Usuário ou senha não cadastrado."
                form = LoginForm()
                return render(request, 'estoque/form_login.html', {'form': form, 'erro': erro})
    #Se o metódo da requisição não é POST, então direcionar para login com um novo formulário.
    form = LoginForm()
    return render(request, 'estoque/form_login.html', {'form': form})

#Função que direciona para página ínicial.
@login_required
def inicio(request):
    return render(request, 'estoque/inicio.html')



#Função para fazer logout.
@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def cadastrar_produto(request):
    if request.method == "POST":
        #Se o método da requisição é POST, receber dados do formulário.
        form = ProdutoForm(request.POST)
        if form.is_valid():
            #Se os dados são válidos salvar o produto no banco de dados.
            produto_novo = form.save()
            if produto_novo is not None:
                #Se o produto novo foi salvo com sucesso, retornar para página de cadastro de produto
                #  com novo formulário e mensagem de sucesso.
                form = ProdutoForm()
                mensagem_confirmacao = "Produto cadastrado."
                return render(request, 'estoque/form_cadastro_produto.html',{'form':form, 'mensagem_confirmacao': mensagem_confirmacao})
        else:
            #Se os dados não são válidos retornar erro
            #  de produto já cadastrado para a página do forumlário.
            erro = "Erro: Produto já está cadastrado."
            form = ProdutoForm()
            return render(request, 'estoque/form_cadastro_produto.html', {'form': form, 'erro': erro})
    #Se os método não é POST, direcionar para a página de cadastro
    form = ProdutoForm()
    return render(request, 'estoque/form_cadastro_produto.html', {'form': form})

#Função para realizar compra de produto já cadastrado.
@login_required
def realizar_compra(request):
    if request.method == "POST":
        #Se o método da requisição é POST, receber dados do formulário.
        form = CompraForm(request.POST)
        if form.is_valid():
            #Se os dados são válidos salvar compra no Banco de Dados
            #e retornar para página de compra com novo formulário e mensagem de confirmação.
            form.save()
            menssagem_confirmacao = "Compra Realizada."
            form = CompraForm()
            return render(request, 'estoque/form_compra.html',{'form': form,'mensagem_confirmacao': menssagem_confirmacao})
        else:
            #Se os dados não são válidos, retornar para página de compra
            #com mensagem de erro e instruções para preenchimento e com novo formulário
            erro = "Algum dado está errado. Quantidade mínima 1, preço mínimo R$: 0.01."
            form = CompraForm()
            return render(request, 'estoque/form_compra.html', {'form': form, 'erro': erro})
    #Se o método não for POST, direcionar para página de compra com forumlário.
    form = CompraForm()
    return render(request, 'estoque/form_compra.html', {'form': form})


#Função que recupera compras feitas no Banco de Dados
#e direciona para página de exibição
@login_required
def listar_compras(request):
    lista_compras = Compra.objects.all()
    return render(request, 'estoque/lista_compra.html', {'lista_compras': lista_compras})