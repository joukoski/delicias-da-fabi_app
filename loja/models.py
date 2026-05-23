from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    icone = models.CharField(max_length=10, default='🍰')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome        = models.CharField(max_length=200)
    descricao   = models.TextField()
    preco       = models.DecimalField(max_digits=8, decimal_places=2)
    categoria   = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, related_name='produtos')
    imagem      = models.ImageField(upload_to='produtos/', blank=True, null=True)
    disponivel  = models.BooleanField(default=True)
    destaque    = models.BooleanField(default=False)
    criado_em   = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['-destaque', 'nome']

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome      = models.CharField(max_length=200)
    email     = models.EmailField(unique=True)
    telefone  = models.CharField(max_length=20)
    endereco  = models.TextField(blank=True)
    ativo     = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nome']

    def __str__(self):
        return self.nome
