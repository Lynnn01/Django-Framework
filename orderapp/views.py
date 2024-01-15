from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cartapp.models import Cart, cartItem
from orderapp.models import Order, OrderDetail
from productsapp.models import Product
from cartapp.views import create_cartId

# Create your views here.


@login_required(login_url="/login")
def order(request):
    user = request.user
    total = 0

    if request.method == "POST":
        fullname = request.POST["fullname"]
        phone = request.POST["phone"]
        address = request.POST["address"]
        cart = Cart.objects.get(cart_id=create_cartId(request), customer=user)
        item = cartItem.objects.filter(cart=cart)

        for i in item:
            total += i.product.price * i.quantity
            order = Order.objects.create(
                fullname=fullname,
                phone=phone,
                address=address,
                total=total,
                customer=user,
            )
            order.save()

        for i in item:
            order_detail = OrderDetail.objects.create(
                product=i.product.name,
                price=i.product.price,
                quantity=i.quantity,
                order=order,
            )
            order_detail.save()

            product = Product.objects.get(pk=i.product.id)
            product.stock = int(i.product.stock - order_detail.quantity)
            product.save()
            i.delete()
        cart.delete()

        return render(request, "ordercomplete.html")

    else:
        return render(request, "order.html")
