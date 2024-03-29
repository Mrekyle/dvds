from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import LessonPricing
from .forms import PricingForm

# Create your views here.


@login_required
def driver_portal(request):
    """
        Renders the drivers portal
    """

    template = 'driver_portal.html'

    context = {

    }

    return render(request, template, context)


@login_required
def admin_portal(request):
    """
        Handles Admin portal
    """

    template = 'admin_portal.html'

    context = {
        "from_admin": True,
    }

    return render(request, template, context)


@login_required
def lesson_pricing(request):
    """
        Set lesson pricing
    """

    if not request.user.is_superuser:
        template = 'errors/404.html'
        messages.errors(request, f'Sorry you do not have access to this page.')
        return render(request, template)

    pricing = LessonPricing

    # if request.method.get == 'POST':
    # get what is being sent and save that to the model

    if 'm-h' in request.POST:
        form = PricingForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, f'Price successfully updated')
    elif 'm-b' in request.POST:
        pricing = LessonPricing.save()
        messages.success(request, f'Price successfully updated')
    elif 'm-r' in request.POST:
        pricing = LessonPricing.save()
        messages.success(request, f'Price successfully updated')
    else:
        form = LessonPricing()

    form = LessonPricing()
    template = 'lesson_pricing.html'

    context = {
        'from_admin': True,
        'pricing': pricing,
    }

    return render(request, template, context)
