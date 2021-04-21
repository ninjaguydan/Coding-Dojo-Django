from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    if request.method == "POST":
        product = Product.objects.get(id = request.POST['product_id'])
        quantity_from_form = int(request.POST["quantity"])
        price = float(product.price)
        total_charge = quantity_from_form * price
        print("Charging credit card...")
        new_order = Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
        return redirect("/checkout")
    else: 
        total_quantity = 0
        total_charge_sum = 0
        for order in Order.objects.all():
            total_quantity += order.quantity_ordered
            total_charge_sum += order.total_price
        context = {
            "recent": Order.objects.last(),
            "total_quantity": total_quantity,
            "charge_sum": total_charge_sum,
        }
        return render(request, "store/checkout.html", context)