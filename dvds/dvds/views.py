from django.shortcuts import render


def handler404(request, exception):
    """
        Handles the error 404 page 
    """

    template = '404.html'

    context = {

    }

    return render(request, template, context)


def handler500(request):
    """
        Handles the error 500 page 
    """

    template = '500.html'

    context = {

    }

    return render(request, template, context)
