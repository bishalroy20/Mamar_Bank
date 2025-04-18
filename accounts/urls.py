from django.urls import path , include
from . import views


urlpatterns = [
    path('register/' , views.UserRegistrationView.as_view() , name='register' ),
    path('login/' ,views.UserLoginView.as_view() , name= 'login' ),
    path('profile/' ,views.UserBankAccountUpdateView.as_view() , name= 'profile' ),
    # path('logout/' ,views.UserLogoutView.as_view() , name= 'logout' ),
    path('logout/' , views.user_logout , name='logout'),
]