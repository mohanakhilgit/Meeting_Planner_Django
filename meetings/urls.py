from django.urls import path
from . import views

urlpatterns = [
    path('<int:meeting_id>', views.details, name='details'),
    path('rooms', views.rooms_list, name='rooms'),
    path('form', views.create_form, name='form')
]
