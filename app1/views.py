from django.shortcuts import render
from .models import Order
from .utils import calculate_price

def order(request):
    if request.method == 'POST':
        academic_level = request.POST['academic_level']
        service_type = request.POST['service_type']
        currency = request.POST['currency']
        price = calculate_price(academic_level, service_type, currency)
        order = Order(academic_level=academic_level, service_type=service_type, currency=currency)
        order.save()
        return render(request, 'order.html', {'price': price, 'currency':currency, "academic_level": academic_level})
    else:
        return render(request, 'order.html')