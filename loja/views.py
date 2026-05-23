from django.shortcuts import render, get_object_or_404
from .models import Produto, Categoria

def home(request):
    destaques   = Produto.objects.filter(disponivel=True, destaque=True)[:6]
    categorias  = Categoria.objects.all()
    return render(request, 'loja/home.html', {
        'destaques': destaques,
        'categorias': categorias,
    })

def produtos(request):
    categoria_id = request.GET.get('categoria')
    busca        = request.GET.get('busca', '')
    categorias   = Categoria.objects.all()
    lista        = Produto.objects.filter(disponivel=True)

    if categoria_id:
        lista = lista.filter(categoria_id=categoria_id)
    if busca:
        lista = lista.filter(nome__icontains=busca)

    categoria_atual = None
    if categoria_id:
        categoria_atual = Categoria.objects.filter(id=categoria_id).first()

    return render(request, 'loja/produtos.html', {
        'produtos': lista,
        'categorias': categorias,
        'categoria_atual': categoria_atual,
        'busca': busca,
    })

def detalhe_produto(request, pk):
    produto    = get_object_or_404(Produto, pk=pk, disponivel=True)
    relacionados = Produto.objects.filter(
        categoria=produto.categoria, disponivel=True
    ).exclude(pk=pk)[:4]
    return render(request, 'loja/detalhe.html', {
        'produto': produto,
        'relacionados': relacionados,
    })
