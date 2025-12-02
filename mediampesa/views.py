from os import times
import requests #we use this lib in python to interact with APIs
from django.shortcuts import render,redirect
from django.db.models.expressions import result
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponse# json format for our results as well queries
from .models import transactions
import base64
from datetime import datetime
import json
from django.core.email import send_mail
from django.core.paginator import Paginator
from dotenv import load_dotenv

load_dotenv()# making our settings config available to our view files
  
# create your views here.
# helper class for transaction security :: Auth token :: access the API routes from daraja mpesa
##authorization
class MpesaPassword:
    pass

# get the access token from mpesa
def index(request):
    pass

#index page for transaction
def index(request):
    pass

# this willexecute an stk push on request
@csrf_exempt
def stk_push(request):
    pass

@csrf_exempt
def mpesa_callback(request):
    pass

# waiting page
def waiting_page(request,transaction_id):
    pass

# check and update status pending complete
def check_status(request,transaction_id):
    pass

# helper function- render payment successful,render payment failed, render payment cancelled
def payment_successful(request):
    pass

def payment_failed(request):
    pass

def payment_cancelled(request):
    pass