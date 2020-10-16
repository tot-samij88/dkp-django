from django.shortcuts import render
from .models import AcardionSlider

def product(request):
    product_slider = AcardionSlider.objects.all()
    context = {
        'product_slider': product_slider,
    }
    return render(request,'pages/product.html',context)
