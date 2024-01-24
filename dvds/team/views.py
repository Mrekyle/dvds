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


def team_detail(request):
    """
        Renders the team detail view page
    """

    template = 'team_detail.html'

    context = {

    }

    return render(request, template, context)
