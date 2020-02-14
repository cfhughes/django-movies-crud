from django.urls import path
from . import views

# NO LEADING SLASHES
urlpatterns = [
    path('', views.index, name='index'),
    path('create_movie', views.create_movie, name='create_movie'),
    path('edit_movie/<int:id>', views.edit_movie, name='edit_movie'),
    path('add_actor/<int:id>', views.add_actor, name='add_actor'),
    path('actor/<int:id>', views.show_actor, name='show_actor'),
    path('delete_movie/<int:id>', views.delete_movie, name='delete_movie')
]