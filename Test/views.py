from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import EmailMessage
# Create your views here.
def index(request):
	msg = EmailMessage(
	    'Subject here',
	    'cổng 25 là ok nhất',
	    to=['quyduong.marketer@gmail.com'],
	)
	msg.send()
	return HttpResponse('success sending')