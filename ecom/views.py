from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import product, Category, cart
from django.contrib.auth.decorators import login_required



# Create your views here.
def frontpage(request):
    products = product.objects.all
    category = Category.objects.all()
    name = [] 
    for categorys in category:
        name.append(categorys.name)
    
    return render(request, 'ecom/frontpage.html', { 'name': name, 'product': products})


@login_required
def detail(request, product_id1):
    product1 = get_object_or_404(product, pk=product_id1)
    if request.method == 'POST':    
        carts = cart()
        in_cart = cart.objects.filter(products=product1)
        if in_cart:
            return HttpResponse("product is already on cart")
        
        carts.products = product1
        carts.customer = request.user        
        carts.save()

    return render(request, 'ecom/detail.html', {'product':product1})


def cart1(request):
    cart1 = cart.objects.filter(customer=request.user)
   
    return render(request,'ecom/cart.html', {'cart': cart1})