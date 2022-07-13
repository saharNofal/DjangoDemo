from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory
from .models import Product, User


def Home(request):
    return render(request, "products/Home.html")


def Users(request):
    return render(request, "products/Users.html", {"users": User.objects.all()})


UserForm = modelform_factory(User, exclude=[])


def addUser(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Users")
    else:
        form = UserForm()
    return render(request, "products/addUser.html", {"form": form})


def Products(request):
    return render(request, "products/Products.html", {"products": Product.objects.all()})


def productDetail(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, "products/productDetail.html", {"product": product})
