from .forms import ContactForm
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage, BadHeaderError
from django.http import HttpResponse
from django.template.loader import get_template
from django.conf import settings


def home(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = settings.DEFAULT_FROM_EMAIL
            to = settings.DEFAULT_TO_EMAIL
            template = get_template('portfolio/contact_template.txt')
            context = {
                'name': name,
                'phone_number': phone_number,
                'email': email,
                'message': message,
            }
            content = template.render(context)
            try:
                EmailMessage(subject, content, from_email, [to], headers={'Reply-To': email}).send()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            form.save()
            return redirect('success')
    return render(request, "portfolio/Home.html", {'form': form})


def success_view(request):
    return render(request, "portfolio/Success.html", {})


