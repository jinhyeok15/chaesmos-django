from django.urls import path
from . import views

from commons.views import (
    INDEX_VIEW_NAME,
    SIGNUP_VIEW_NAME,
    LOGIN_VIEW_NAME,
    LOGOUT_VIEW_NAME,
    WRITE_VIEW_NAME,
    SOLVE_VIEW_NAME,
    SUCCESS_VIEW_NAME,
    READ_LETTERS_VIEW_NAME
)


urlpatterns = [
    path('', views.index, name=INDEX_VIEW_NAME),
    path('success/', views.success, name=SUCCESS_VIEW_NAME),
    path('signup/', views.signup, name=SIGNUP_VIEW_NAME),
    path('login/', views.login, name=LOGIN_VIEW_NAME),
    path('logout/', views.logout, name=LOGOUT_VIEW_NAME),
    path('postoffice/write/', views.write, name=WRITE_VIEW_NAME),
    path('postoffice/solve/', views.solve, name=SOLVE_VIEW_NAME),
    path('mymails/', views.read_letters, name=READ_LETTERS_VIEW_NAME),
]
