from django.shortcuts import render
from . forms import SupportForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def index(request):
    """
        Renders the home page of the application
    """

    template = 'index.html'

    context = {

    }

    return render(request, template, context)


def contact(request):
    """
        Renders the contact page of the application
    """

    template = 'contact.html'
    form = SupportForm()

    if request.method == 'POST':
        form = SupportForm(request.POST)
        if form.is_valid():
            contact = form.save()

            """
                Contact email handling
            """

            name = request.POST.get('name')
            email = request.POST.get('email')
            number = request.POST.get('number')
            location = request.POST.get('location')
            gearbox = request.POST.get('gearbox')
            information = request.POST.get('information')
            message = request.POST.get('message')
            subject = 'New contact form request'

            contact_message = f"""
                You have received a new message from {name}
                -------------------------------------------

                They have asked:

                {message}

                Contact them at:

                Phone Number: {number}
                Email: {email}

                -------------------------------------------

                Location: {location}
                Gearbox Preference: {gearbox}
                How they heard about DVD'S: {information}

                -------------------------------------------
            """

            send_mail(
                subject=subject,
                message=contact_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL]
            )
            messages.success(
                request, f'Success! Your message was sent successfully and we will be in touch as soon as we can.')
            return render(request, template)
        else:
            form = SupportForm()
            messages.error(
                request, f'Oops, somethings gone wrong. Please try again later.')
            return render(request, template)

    context = {
        'form': form,
    }

    return render(request, template, context)


def privacy(request):
    """
        Renders the privacy policy
    """

    template = 'privacy-policy.html'

    context = {

    }

    return render(request, template, context)


def terms(request):
    """
        Renders terms and conditions
    """

    template = 'terms.html'

    context = {

    }

    return render(request, template, context)
