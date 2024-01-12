from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from productsapp.models import Product
from cartapp.models import Cart, cartItem

# Create your views here.


def create_cartId(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


@login_required(login_url="/login")
def cart(request):
    user = request.user
    counter = 0
    total = 0
    try:
        cart = Cart.objects.get(cart_id=create_cartId(request), customer=user)
        item = cartItem.objects.filter(cart=cart)
        for i in item:
            counter += i.quantity
            total += i.quantity * i.product.price
    except (Cart.DoesNotExist, cartItem.DoesNotExist):
        cart = None
        Item = None
    return render(
        request, "cart.html", {"item": item, "counter": counter, "total": total}
    )


@login_required(login_url="/login")
def addCart(request, product_id):
    product = Product.objects.get(pk=product_id)
    # create a new cart
    try:
        # have a cart
        cart = Cart.objects.get(cart_id=create_cartId(request))
    except Cart.DoesNotExist:
        # haven't a cart
        cart = Cart.objects.create(
            cart_id=create_cartId(request), customer=request.user
        )
        cart.save()

    # save the items list on the cart
    try:
        # add same item
        item = cartItem.objects.get(product=product, cart=cart)
        if item.quantity < item.product.stock:
            item.quantity += 1
            item.save()
    except cartItem.DoesNotExist:
        # add new item
        item = cartItem.objects.create(product=product, cart=cart, quantity=1)
        item.save()

    return redirect("/cart")
