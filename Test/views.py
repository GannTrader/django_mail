from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
# Create your views here.
def index(request):
	send_mail(
	    'Subject here',
	    'Here is the message.',
	    'annakimsohappy@gmail.com',
	    ['quyduong.marketer@gmail.com'],
	    fail_silently=False,
	)
	return HttpResponse('success sending')