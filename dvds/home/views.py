from django.shortcuts import render

# Create your views here.


def index(request):
    """
        Renders the home page of the application
    """

    template = 'index.html'

    context = {

    }

    return render(request, template, context)
