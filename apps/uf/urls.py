from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='ufs_index'),
    # path('<int:uf_id>', uf, name='uf'),
    # path('buscar', busca, name='buscar'),
    path('create', create_uf, name='create_uf'),
    path('delete/<int:uf_id>', delete_uf, name='delete_uf'),
    path('edit/<int:uf_id>', edit_uf, name='edit_uf'),
    path('update_uf', update_uf, name='update_uf')
]