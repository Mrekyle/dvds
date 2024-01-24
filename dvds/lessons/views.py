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


def automatic(request):
    """
        Renders the automatic pricing page of the application

    """

    template = 'automatic.html'

    context = {

    }

    return render(request, template, context)


def instructor(request):
    """
        Renders the instructor pricing page of the application

    """

    template = 'instructor.html'

    context = {

    }

    return render(request, template, context)


def intensive(request):
    """
        Renders the intensive lessons pricing page of the application

    """

    template = 'intensive.html'

    context = {

    }

    return render(request, template, context)


def refresher(request):
    """
        Renders the refresher lesson pricing page of the application

    """

    template = 'refresher.html'

    context = {

    }

    return render(request, template, context)


def theory_test(request):
    """
        Renders the theory and driving test page of the application

    """

    template = 'theory_test.html'

    context = {

    }

    return render(request, template, context)


def weekly(request):
    """
        Renders the weekly lesson pricing page of the application

    """

    template = 'weekly.html'

    context = {

    }

    return render(request, template, context)
