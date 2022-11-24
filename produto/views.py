from django.shortcuts import redirect ,render , HttpResponseRedirect
from .forms import AdicionarProduto
from .models import Produto
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


@staff_member_required
def cadastrar(request):
    if request.method == 'POST':
        fm = AdicionarProduto(request.POST)
        if fm.is_valid():
            nome_produto = fm.cleaned_data['nome_produto']
            slug = fm.cleaned_data['slug']
            descricao = fm.cleaned_data['descricao']
            preco = fm.cleaned_data['preco']
            qtd_produto = fm.cleaned_data['qtd_produto']
            reg = Produto(nome_produto=nome_produto, slug=slug, descricao=descricao, preco=preco, qtd_produto=qtd_produto)
            reg.save()
            fm = AdicionarProduto()
    else:
        fm = AdicionarProduto()
    produtos = Produto.objects.all()
    return render(request, 'cadastrar.html', {'form': fm, 'produto': produtos})

def atualizar(request,id):
    if request.method == 'POST':
        pi = Produto.objects.get(pk=id)
        fm = AdicionarProduto(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('index')
    else:
        pi = Produto.objects.get(pk=id)
        fm = AdicionarProduto(instance=pi)

    return render(request, 'atualizar.html',{'form':fm})


def deletar(request,id):
    if request.method == 'POST':
        pi = Produto.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


@login_required
def index(request):
    produtos = Produto.objects.all()
    return render(request, 'index.html', {'produto': produtos})


def comprar(request,id):
    comprar = Produto.objects.get(id=id)
    comprar.qtd_produto -= 1
    comprar.save()
    return HttpResponseRedirect('/')