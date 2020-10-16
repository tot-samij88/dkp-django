from django.shortcuts import render
from .models import OurTeamate


def team(request):
    our_teamate = OurTeamate.objects.all()
    context = {
        'our_teamate': our_teamate,

    }
    return render(request, 'pages/team.html', context)
