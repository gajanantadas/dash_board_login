from . import views
from django.urls import path
urlpatterns = [
    path('sign/',views.register_view , name='sign_up'),
    path('dash/',views.DashBoardView,name='dashboard'),
    path('login/',views.LoginView, name='Log_In'),
    path('logout/',views.logout_view, name='Log_Out'),
]
