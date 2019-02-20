from django.shortcuts import render, redirect
import random
from time import gmtime, strftime

def index(request):
  if 'gold' not in request.session:
    request.session['gold']=0
    request.session['event_list']=[]
  return render(request,'index.html')

def process_money(request):
  if request.POST['location']=='farm':
    num=random.randint(10,20)
  if request.POST['location']=='cave':
    num=random.randint(5,10)
  if request.POST['location']=='house':
    num=random.randint(2,5)
  if request.POST['location']=='casino':
    num=random.randint(-50,50)
  print(num)
  request.session['gold']+=num
  
  location=request.POST['location']
  if num<0:
    status="Lost"
  else:
    status="Earn"
  time=strftime("%Y-%m-%d %H:%M %p", gmtime())
  event = f"{status} {num} golds from the {location} ({time})"
  print(event)
  request.session['event_list'].append(event)

  return redirect('/')
