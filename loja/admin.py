from django.contrib import admin
from django.utils.html import format_html
from .models import Categoria, Produto, Cliente


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display  = ('icone', 'nome', 'descricao', 'total_produtos')
    search_fields = ('nome',)

    def total_produtos(self, obj):
        return obj.produtos.count()
    total_produtos.short_description = 'Produtos'


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display   = ('preview_imagem', 'nome', 'categoria', 'preco_formatado', 'disponivel', 'destaque', 'criado_em')
    list_filter    = ('categoria', 'disponivel', 'destaque')
    search_fields  = ('nome', 'descricao')
    list_editable  = ('disponivel', 'destaque')
    list_per_page  = 20
    fieldsets = (
        ('Informações do Produto', {
            'fields': ('nome', 'descricao', 'categoria', 'imagem')
        }),
        ('Preço e Disponibilidade', {
            'fields': ('preco', 'disponivel', 'destaque')
        }),
    )

    def preco_formatado(self, obj):
        return f'R$ {obj.preco:.2f}'.replace('.', ',')
    preco_formatado.short_description = 'Preço'

    def preview_imagem(self, obj):
        if obj.imagem:
            return format_html('<img src="{}" style="width:50px;height:50px;object-fit:cover;border-radius:6px;">', obj.imagem.url)
        return '📷'
    preview_imagem.short_description = 'Foto'


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display  = ('nome', 'email', 'telefone', 'ativo', 'criado_em')
    list_filter   = ('ativo',)
    search_fields = ('nome', 'email', 'telefone')
    list_editable = ('ativo',)
    list_per_page = 20


# Personalizar o painel admin
admin.site.site_header  = '🍰 Delícias da Fabi — Painel Administrativo'
admin.site.site_title   = 'Delícias da Fabi'
admin.site.index_title  = 'Gerenciamento da Loja'
