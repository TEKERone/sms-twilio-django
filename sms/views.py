#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse
@csrf_exempt
def sms_response(request):
    # Start our TwiML response
    resp = MessagingResponse()
    # Add a text message
    msg = resp.message("Hello, TEKER!")
    return HttpResponse(str(resp))