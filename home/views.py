from django.shortcuts import render
from .models import FirstSlide
from .models import NextSlide


def home(request):
    first_slide = FirstSlide.objects.all()
    next_slide = NextSlide.objects.all()
    context = {
        'first': first_slide,
        'next': next_slide,
    }

    return render(request, 'pages/index.html', context)
