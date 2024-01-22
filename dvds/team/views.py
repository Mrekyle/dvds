from django.shortcuts import render

# Create your views here.


def team(request):
    """
        Renders the team page
    """

    template = 'team.html'

    context = {

    }

    return render(request, template, context)
