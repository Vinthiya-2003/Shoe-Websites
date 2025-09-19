from django.shortcuts import render

def home(request):
    return render(request, "shoe/home.html")

def about(request):
    return render(request, "shoe/about.html")

def contact(request):
    return render(request, "shoe/contact.html")

def login_view(request):
    return render(request, "shoe/login.html")

def cart(request):
    return render(request, "shoe/cart.html")

def womens(request):
    return render(request, "shoe/womens.html")

def mens(request):
    return render(request, "shoe/mens.html")

def kids(request):
    return render(request, "shoe/kids.html")

def brands(request):
    return render(request, "shoe/brands.html")

def offers(request):
    return render(request, "shoe/offers.html")

def order(request):
    return render(request, "shoe/order.html")

def checkout(request):
    return render(request, "shoe/checkout.html")

def trackorder(request):
    return render(request, "shoe/trackorder.html")

def thanks(request):
    return render(request, "shoe/thanks.html")