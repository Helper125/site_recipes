from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, logout as auth_logout, login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Recipes_UA_EN, CommentUsers
from .forms import Register

import logging
import google.generativeai as genai
import google.api_core as exceptions
import os
from dotenv import load_dotenv

# Create your views here.
logger = logging.getLogger(__name__)

GIMINI_KEY = os.getenv("GIMINI_KEY")
GIMINI_KEY2 = os.getenv("GIMINI_KEY2")

# CHAT_GPT_KEY = os.getenv("CHAT_GPT_KEY")
# CHAT_GPT_KEY2  = os.getenv("CHAT_GPT_KEY2")

genai.configure(api_key=GIMINI_KEY)

model = genai.GenerativeModel("models/gemini-1.5-flash")

def index_ua(request):
    logging.debug("good")
    logging.error("problem")
    search_recipes = request.GET.get('search')
    if search_recipes:
        recipes = Recipes_UA_EN.objects.filter(name_ua__iregex=search_recipes) | Recipes_UA_EN.objects.filter(name_en__iregex=search_recipes)
    else:
        recipes = Recipes_UA_EN.objects.all()
    paginator = Paginator(recipes, 10)
    if 'page' in request.GET:
        page_num = request.GET.get('page', 2)
    else:
        page_num = 1
    page = paginator.get_page(page_num) 
    return render(request, 'index_ua.html', {"recipes":page.object_list, "page":page })

def index_en(request):
    logging.debug("good")
    logging.error("problem")
    search_recipes = request.GET.get('search')
    if search_recipes:
        recipes = Recipes_UA_EN.objects.filter(name_en__iregex=search_recipes) | Recipes_UA_EN.objects.filter(name_ua__iregex=search_recipes)
    else:
        recipes = Recipes_UA_EN.objects.all()
    paginator = Paginator(recipes, 10)
    if 'page' in request.GET:
        page_num = request.GET.get('page', 2)
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    return render(request, 'index_en.html', {"recipes":page.object_list, "page":page})


def registerUser(request):
    if request.method == "POST":
        form = Register(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("index_ua")
    else:
        form = Register()
    return render(request, 'user/register.html', {'form':form})


@login_required
def logout(request):
    auth_logout(request)
    return redirect("index_ua")


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("index_ua")
        else:
            messages.error(request, "не вірний логін або пароль. / Incorrect login or password.")


    return render(request, 'user/login.html')

def recipes_more(request, id):
    recipe = get_object_or_404(Recipes_UA_EN, id=id)
    comment = CommentUsers.objects.filter(recipe=recipe)
    paginator = Paginator(comment, 10)
    if 'page' in request.GET:
        page_num = request.GET.get('page', 2)
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    if request.method == 'POST':
        comment = request.POST.get('comment')

        createcomment = CommentUsers.objects.create(
            user=request.user,
            recipe=recipe,
            comment=comment
        )
   
        return redirect('recipes_more', id=id)
    return render(request, "recipes_more.html", {"recipe":recipe, "comment":page.object_list, 'page':page})

def recipes_more_en(request, id):
    recipe = get_object_or_404(Recipes_UA_EN, id=id)
    comment = CommentUsers.objects.filter(recipe=recipe)
    paginator = Paginator(comment, 10)
    if 'page' in request.GET:
        page_num = request.GET.get('page', 2)
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    if request.method == 'POST':
        comment = request.POST.get('comment')

        createcomment = CommentUsers.objects.create(
            user=request.user,
            recipe=recipe,
            comment=comment
        )
   
        return redirect('recipes_more_en', id=id)
    return render(request, "recipes_more_en.html", {"recipe":recipe, "comment":page.object_list, 'page':page})

def delete_comment(request, id_comment):
    comment = get_object_or_404(CommentUsers, id=id_comment)
    recipe_id = comment.recipe.id
    if request.user == comment.user:
        comment.delete()
    return redirect('recipes_more', id=recipe_id)

def delete_comment_en(request, id_comment):
    comment = get_object_or_404(CommentUsers, id=id_comment)
    recipe_id = comment.recipe.id
    if request.user == comment.user:
        comment.delete()
    return redirect('recipes_more_en', id=recipe_id)

def Gimini_transtale(text, source_lang="ukrainian", target_lang="English"):
    promo = f"Hello, I translated the text {source_lang} to {target_lang} and now I'm going to do a translation without a full description. Thank you very much.:\n\n{text}"
    response = model.generate_content(promo)
    return response.text.strip()


def translation_bd(request):
    if request.method == "POST":
        name_ua = request.POST.get('name')
        description_ua = request.POST.get('description')
        instruction_ua = request.POST.get('instruction')
        img = request.POST.get('img')

        try:
            name_en = Gimini_transtale(name_ua)
            description_en = Gimini_transtale(description_ua)
            instruction_en = Gimini_transtale(instruction_ua)
        
            Recipes_UA_EN.objects.create(
                name_ua=name_ua,
                description_ua=description_ua,
                instruction_ua=instruction_ua,
                name_en=name_en,
                description_en=description_en,
                instruction_en=instruction_en,
                img=img
            )
            messages.success(request, "okey/ок")
        except Exception as e:
            messages.error(request, f"error: {e}")

    return render(request, 'created_recipes.html')