from django.urls import path

from tags.views import index, create, show, update, delete


urlpatterns = [
    path('list', index ),
    path('create', create ),
    path('show/<int:id>', show ),
    path('update/<int:id>', update ),
    path('delete/<int:id>', delete )
]
