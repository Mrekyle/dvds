from django.shortcuts import render

# Create your views here.


def pricing(request):
    """
        Renders the main pricing page of the application

    """

    template = 'pricing.html'

    context = {

    }

    return render(request, template, context)
