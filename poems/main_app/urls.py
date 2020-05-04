from django.urls import path
from . import views

urlpatterns = [
 path('', views.home, name='home'),
 path('about/', views.about, name ='about'),
 path('accounts/signup/', views.signup, name='signup'),
 path('poems/', views.poems_index, name ='index'),
 path('poems/<int:pk>/', views.poems_detail, name='detail'),
 path('poems/<int:poem_id>/add_comment/', views.add_comment, name='add_comment'),
 path('poems/create', views.PoeCreate.as_view(), name='poes_create'),
 path('index/<int:pk>/update/', views.PoeUpdate.as_view(), name='poes_update'),
 path('index/<int:pk>/delete', views.PoeDelete.as_view(), name='poes_delete'),
]