from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('login/', views.login_view, name="login"),
    path('cart/', views.cart, name="cart"),
    path('womens/', views.womens, name="womens"),
    path('mens/', views.mens, name="mens"),
    path('kids/', views.kids, name="kids"),
    path('checkout/', views.checkout, name="checkout"),
    path('trackorder/', views.trackorder, name="trackorder"),
    path('thanks/', views.thanks, name="thanks"),

    
]
