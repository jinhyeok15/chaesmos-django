from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name=views.INDEX_VIEW_NAME),
    path('signup/', views.signup, name=views.SIGNUP_VIEW_NAME),
    path('login/', views.login, name=views.LOGIN_VIEW_NAME),
    path('logout/', views.logout, name=views.LOGOUT_VIEW_NAME),
]
