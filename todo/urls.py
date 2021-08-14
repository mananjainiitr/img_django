from django.urls import path

from .views import index, detail, create,update,delete

app_name='todo'
urlpatterns = [
    path('', index, name='index'),
    path('<int:list_id>/', detail, name='list_details'),
    path('createlist/', create, name='list_create'),
    path('update/',update, name='update_list'),
    path('delete/',delete, name='delete_list'),


]