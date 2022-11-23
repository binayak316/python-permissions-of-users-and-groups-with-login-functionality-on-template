from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('login-user', views.login_user, name="login"),
    path('register-user', views.register_user, name="register"),
    path('logout-user', views.logout_user, name='logout'),

    path('add-employee', views.add_employee, name="addEmployee"),
    path('update-employee/<int:pk>', views.update_employee, name="update-employee"),
    path('delete-employee/<int:pk>', views.delete_employee, name="delete-employee"),
    path('app', views.app, name="app"),
]