from django.shortcuts import render, reverse, redirect
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
        if request.method == 'POST':
            if form.is_valid():
                support_form = form.save()
                messages.success(
                    request, f'Success! Message sent successfully, We will be in touch as soon as possible.')

            """
                Contact email handling
            """

            name = request.POST.get('name')
            email = request.POST.get('email')
            number = request.POST.get('number')
            location = request.POST.get('location')
            gearbox = form.cleaned_data['gearbox']
            information = form.cleaned_data['information']
            message = request.POST.get('message')
            send_copy = request.POST.get('send-copy')
            subject = 'New contact form request'
            subject_copy = 'Your message to Dedham Vale Driving School'

            if send_copy == 'on':
                """
                    Send a copy to the user
                """

                message_copy = f""""

                    {name} you have sent an email request to Dedham Vale Driving School.
                    They will be in touch as soon as possible.
                    --------------------------------------------

                    Your message contains:

                    {message}

                    Email - {email}
                    Number - {number}
                    Your Location - {location}
                    Gearbox Preference - {gearbox}
                    How you hear about Dvd's - {information}
                    
                    --------------------------------------------
                """

                send_mail(
                    subject=subject_copy,
                    message=message_copy,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[email]
                )

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
                request, f'Success! Message sent successfully, We will be in touch as soon as possible.')
            return redirect(reverse('home'))
        else:
            messages.error(request, f'Oops, something went wrong. Please try again later. \
                           If the problem persists, please email directly.')
    else:
        form = SupportForm()

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
