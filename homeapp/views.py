from django.shortcuts import render
from django.core.mail import send_mail
from .forms import EmailForm


# Create your views here.
def index(r):
    return render(r,r'homeapp/index.html')

def oldindex(r):
    return render(r,r"oldwebsite/index.html")

def todohome(r):
    return render(r,r"listodo/index.html")

# views.py
def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            full_message = f"From: {name}\nEmail: {email}\n\n{message}"

            send_mail(
                subject=subject,
                message=full_message,
                from_email=email,
                recipient_list=['sunnyraperia1@gmail.com'],
                fail_silently=False,
            )
            return render(request, r'homeapp/index.html', {'sent_message': True})
    return render(request, 'homeapp/index.html', {'sent_message': False})


def portfolio(r):
    return render(r,r'portfolio/index.html')