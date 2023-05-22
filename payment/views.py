from django.shortcuts import render, HttpResponse
# import razorpay 
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def payment(request):
    return render(request, "payment/payment.html")


@csrf_exempt
def success(request):
    return render(request, "payment/success.html")