from django.http import HttpResponse
from django.urls import path

from tags.views import index, create, show, update, delete

urlpatterns = [
    path('', index, name="tags-list" ),
    path('create', create, name="tags-create" ),
    path('show/<int:id>', show, name="tags-show" ),
    path('update/<int:id>', update, name="tags-update" ),
    path('delete/<int:id>', delete, name="tags-delete" ),
]
