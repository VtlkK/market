from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RegisterForm, OrderForm, ProductForm
from .models import Product, Order_qq


# Create your views here.

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            messages.info(request, 'Invalid Username or Password')
    return render(request, 'login.html')

def index(request):
    shirts = Product.objects.filter(product_item_id=1)
    shorts = Product.objects.filter(product_item_id=2)
    pants = Product.objects.filter(product_item=4)
    hats = Product.objects.filter(product_item=5)
    jackets = Product.objects.filter(product_item=6)




    return render(request, 'index.html', {'shirts': shirts, 'shorts': shorts, 'pants': pants, 'hats': hats, 'jackets':jackets})

def logout_view(request):
    logout(request)

def order(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order.product = product
            order_form.save()
            return redirect("index")
    else:
        order_form = OrderForm(initial={'product': product})


    return render(request, 'order.html', {'order_form': order_form, 'product': product})

def product_post(request):
    form = ProductForm
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("product_post")
    return render(request, 'product_post.html', {'form': form})



def order_list(request):
    order_list = Order_qq.objects.all()
    return render(request, 'order_list.html', {'order_list': order_list})








