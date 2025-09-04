from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, logout as auth_logout, login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages

from recipes_straw.models import Recipes_UA_EN

# Create your views here.

def add_to_cart(request, recipes_id):
    recipes = get_object_or_404(Recipes_UA_EN, id=recipes_id)
    cart = request.session.get('cart', {})

    recipes_id_str = str(recipes_id)
    cart[recipes_id_str] = {
        'name': recipes.name_ua
    }
    request.session['cart'] = cart
    return redirect('/')

def remove_cart(request, recipes_id):
    cart = request.session.get('cart', {})
    recipes_id_str = str(recipes_id)
    if recipes_id_str in cart:
        del cart[recipes_id_str]
        request.session['cart'] = cart
    return redirect('cart_detail')

def cart_detail(request):
    cart = request.session.get('cart', {})
    return render(request, 'cart.html', {"cart":cart})


def add_to_cart_en(request, recipes_id):
    recipes_en = get_object_or_404(Recipes_UA_EN, id=recipes_id)
    cart = request.session.get('cart', {})
    recipes_id_str = str(recipes_id)
    cart[recipes_id_str] = {
        'name': recipes_en.name_en
    }
    request.session['cart'] = cart
    return redirect('index_en')

def remove_cart_en(request, recipes_id):
    cart = request.session.get('cart', {})
    recipes_id_str = str(recipes_id)
    if recipes_id_str in cart:
        del cart[recipes_id_str]
        request.session['cart'] = cart
    return redirect('cart_detail_en')

def cart_detail_en(request):
    cart = request.session.get('cart', {})
    return render(request, 'cart_en.html', {"cart":cart})