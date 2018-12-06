
from django.urls import path
from album import views

urlpatterns = [
    path('<int:media_id>/', views.media_page, name='media'),
    path('<int:media_id>/edit/', views.media_edit, name='media'),
    path('add/', views.media_add, name='media_add'),
    path('add-by-insta-link/', views.media_add_insta, name='media_add_insta'),
    path('mine/', views.media_mine, name='media_mine')
]
