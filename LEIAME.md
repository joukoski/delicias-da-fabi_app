# Delícias da Fabi — CRUD Django

## Instalação

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata loja/fixtures/dados_iniciais.json
python manage.py createsuperuser
python manage.py runserver
```

## Acessos

- **Site público:** http://127.0.0.1:8000
- **Painel Admin:** http://127.0.0.1:8000/admin

## Estrutura

- `loja/models.py` — Modelos: Categoria, Produto, Cliente
- `loja/admin.py` — Configuração do painel administrativo
- `loja/views.py` — Views do site público
- `loja/urls.py` — Rotas do site
- `templates/` — Templates HTML
- `static/css/` — Estilos CSS
