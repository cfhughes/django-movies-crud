from django.urls import path
from . import views

# NO LEADING SLASHES
urlpatterns = [
    path('', views.index, name='index'),
    path('create_movie', views.create_movie, name='create_movie'),
    path('edit_movie/<int:id>', views.edit_movie, name='edit_movie'),
    path('delete_movie/<int:id>', views.delete_movie, name='delete_movie')
]