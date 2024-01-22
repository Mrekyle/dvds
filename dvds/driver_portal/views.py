from django.shortcuts import render

# Create your views here.


def driver_portal(request):
    """
        Renders the drivers portal
    """

    template = 'driver_portal.html'

    context = {

    }

    return render(request, template, context)
