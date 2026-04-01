from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from datetime import datetime

from django.shortcuts import render

def home(request):
    return render(request, 'portfolio/home.html')

def about(request):
    return render(request, 'portfolio/about.html')

def projects(request):
    return render(request, 'portfolio/projects.html')

def contact(request):
    return render(request, 'portfolio/contact.html')

def service(request):
    return render(request, 'portfolio/service.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        subject = f"Portfolio Message from {name}"
        body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        try:
            send_mail(
                subject,
                body,
                email,
                ['nsokemmanuelfavour@gmail.com'],  # change this later
                fail_silently=False
            )
            messages.success(request, "Message sent successfully!")
        except Exception as e:
            print(e)  # 👈 VERY IMPORTANT for debugging
            messages.error(request, "Something went wrong. Try again.")

            from django.shortcuts import render
from datetime import datetime

def home(request):
    return render(request, 'portfolio/home.html', {'current_year': datetime.now().year})

def about(request):
    return render(request, 'portfolio/about.html', {'current_year': datetime.now().year})

def projects(request):
    return render(request, 'portfolio/projects.html', {'current_year': datetime.now().year})

def contact(request):
    return render(request, 'portfolio/contact.html', {'current_year': datetime.now().year})

from django.core.mail import send_mail
from django.shortcuts import render
from django.conf import settings

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

        send_mail(
            subject=f"New Contact Form Message from {name}",
            message=full_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
        )

        return render(request, 'portfolio/contact.html', {
            'success': True
        })

    return render(request, 'portfolio/contact.html')

print(settings.EMAIL_HOST_USER)
