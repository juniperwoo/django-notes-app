# notes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # homepage
    path('notes/', views.get_notes, name='get_notes'),  # fetch notes (API)
    path('notes/add/', views.add_note, name='add_note'),  # add note
    path('notes/toggle/<int:id>/', views.toggle_important),
    path('notes/delete/<int:id>/', views.delete_note, name='delete_note'),  # delete note
  path('signup/', views.signup_view, name='signup')

]