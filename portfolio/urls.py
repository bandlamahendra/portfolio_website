from django.urls import path
from portfolio import views


urlpatterns = [
    path('',views.home),
    path('basic/',views.basic,name='basic'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('resume/',views.resume,name='resume'),
    path('portfolio/',views.portfolio,name='portfolio'),
    path('services/',views.services,name='services'),
    path('blog/',views.blog,name='blog'),
    path('custom_blog/',views.custom_blog,name='custom_blog'),
    path('ecom/',views.ecom,name='ecom'),
]
