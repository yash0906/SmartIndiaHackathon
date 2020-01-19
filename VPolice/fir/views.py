from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.
def index(request):
	return render(request, 'fir/index.html')
	# return HttpResponse('<h1>HELLO</h1>')
def home(request):
	context = {
	'missings' : MissingChildren.objects.all(),
	'stolens' : StolenVehicles.objects.all(),
	}
	return render(request, 'fir/home.html', context)

def addsomething(request):
	missing_form = MissingChild
	stolen_form = StolenVehicle 
	return render(request, 'fir/addcus.html', {'missing_form':missing_form, 'stolen_form':stolen_form})

def missing(request):

	if request.method == 'POST':
		form  = MissingChild(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'fir/thanks.html', {'msg':'Complaint Added Successfully!'})
		else:
			return render(request, 'fir/thanks.html', {'msg':'Complaint Not Added due to technical error!'})
	return index(request)

def stolen(request):

	if request.method == 'POST':
		form  = StolenVehicle(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'fir/thanks.html', {'msg':'Complaint Added Successfully!'})
		else:
			return render(request, 'fir/thanks.html', {'msg':'Complaint Not Added due to technical error!'})
	return index(request)