from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.core.mail import send_mail

# Create your views here.
def index(request):
	send_mail(
	    'Tieu de 1',
	    'Test',
	    'annakimsohappy@gmail.com',
	    ['lavahiw670@inxto.net'],
	    fail_silently=False,
	)
	return HttpResponse('success sending')

def email2(request):
	email = EmailMessage(
	    'Hello',
	    'Body goes here',
	    'annakimsohappy@gmail.com',
	    ['lavahiw670@inxto.net'],
	)
	email.send()
	return HttpResponse('success')