from django.urls import path

from topics.views import index, create, show, update, delete

urlpatterns = [
    path('', index, name="topics-list" ),
    path('create', create, name="topics-create" ),
    path('show/<int:id>', show, name="topics-show" ),
    path('update/<int:id>', update, name="topics-update" ),
    path('delete/<int:id>', delete, name="topics-delete" )
]