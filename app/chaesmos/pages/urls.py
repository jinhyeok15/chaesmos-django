from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='page-index'),
    path('signup/', views.signup, name='page-signup'),
    path('login/', views.login, name='page-login'),
]
