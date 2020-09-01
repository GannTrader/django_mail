from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import EmailMessage

# Create your views here.
def index(request):
	msg = EmailMessage(
	    'Subject here',
	    'body text go here...',
	    'annakimsohappy@gmail.com',
	    ['lavahiw670@inxto.net'],
	)
	msg.send()
	return HttpResponse('success sending')
