from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib import messages
from Base import models
from Base.models import Contact
from django.core.mail import send_mail
from django.conf import settings 
# from django.contrib.auth.decorators import login_required
def home(request):
    return render(request,'home.html')


# @login_required(login_url='')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        number = request.POST.get('phone', '').strip()
        content = request.POST.get('message', '').strip()

        if not name or len(name) < 2 or len(name) > 30:
            messages.error(request, 'Length of name should be between 2 and 30 characters.')
            return render(request, 'home.html')

        if not email or len(email) < 5 or len(email) > 30:
            messages.error(request, 'Invalid email, try again.')
            return render(request, 'home.html')

        if not number or len(number) < 10 or len(number) > 12:
            messages.error(request, 'Invalid number, please try again.')
            return render(request, 'home.html')

        # Save to DB
        ins = Contact(name=name, email=email, number=number, content=content)
        ins.save()

        send_mail(
    subject=f"Mail from {name}",
    message=f"Name: {name}\nEmail: {email}\nPhone: {number}\nMessage: \n{content}",
    from_email=settings.EMAIL_HOST_USER,
    recipient_list=['yrsksanthosh@gmail.com'],  # replace with your actual email
    fail_silently=False,
)


        messages.success(request, 'Thank You for contacting me! Your message has been saved.')
        return redirect('/')  # Or render the same page

    return render(request, 'home.html')

