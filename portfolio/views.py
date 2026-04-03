from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime


def home(request):
    return render(request, 'portfolio/home.html', {
        'current_year': datetime.now().year
    })


def about(request):
    return render(request, 'portfolio/about.html', {
        'current_year': datetime.now().year
    })


def projects(request):
    return render(request, 'portfolio/projects.html', {
        'current_year': datetime.now().year
    })


def service(request):
    return render(request, 'portfolio/service.html', {
        'current_year': datetime.now().year
    })


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        full_message = f"""
New message from your website:

Name: {name}
Email: {email}

Message:
{message}
"""

        try:
            send_mail(
                subject=f"New Contact Form Message from {name}",
                message=full_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
            )
            return render(request, 'portfolio/contact.html', {'success': True})

        except Exception as e:
            print(e)

    return render(request, 'portfolio/contact.html', {
        'current_year': datetime.now().year
    })