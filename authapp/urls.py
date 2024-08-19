from django.urls import path
from authapp import views


urlpatterns = [
    path('signup/',views.signup,name="signup"),
    path('login/',views.h_login,name="login"),
    path('logout/',views.h_logout,name="logout"),
   ]