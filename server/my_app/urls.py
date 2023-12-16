from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path(r'hello/', views.say_hello),
    # path(r'insert/', views.dummy_insert),
    path(r'register/', views.sign_up, name='register'),
    path(r'login/', views.sign_in, name='login'),
    path(r'logout/', views.sign_out, name='logout'),
    path(r'home/', views.home, name='home'),
    path(r'home/create', views.create_post, name='post_create'),
    path(r'home/edit/<int:id>/', views.edit_post, name='post_edit'),
    path(r'home/delete/<int:id>/', views.delete_post, name='post_delete'),
    path(r'', views.default_view, name='default')
]