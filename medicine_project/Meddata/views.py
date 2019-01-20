from django.shortcuts import render,redirect
from rest_framework import generics
from django.shortcuts import HttpResponse
from .models import medicine
from .serializers import MedicineSerializer
from django.views.generic.base import View,TemplateView
from .forms import *
from django.core.exceptions import *

# Create your views here.

	

class ListMedicineView(generics.ListAPIView):											#Used for API 
	#providea get method handler
	queryset = medicine.objects.all()
	serializer_class = MedicineSerializer

def home(request):
	return render (request , 'home.html',context = {'key':value})

# Function based view - Displays a welcome page for the app
def landing(request):                                         	
	context = {}
	template_name = 'landing.html'
	context['user'] = request.user
	return render(request,template_name,context)

# Class method
class SpecMedView(TemplateView):
	template_name =  'specmed.html'

	def post(self,request,*args,**kwargs):												#to send value to server
		get_med_form = GetMedForm(request.POST)
		if get_med_form.is_valid():
			itemcode = get_med_form.cleaned_data.get("ItemCode")						#assign the value to itemcode
			try:
				med = medicine.objects.get(ItemCode=str(itemcode))
				print(med.Descr)                                         				#Displays the information /med.MRP/med.mfg
				return HttpResponse(med.Descr)										
			except ObjectDoesNotExist:													#If the object does not exist
				print("no such medicine")
				return redirect('specmed')
			
		else:
			return HttpResponse("no such medicine")
		pass  	
	def get_context_data(self,*args,**kwargs):											#to get the Displayed at the serve end
		context = super().get_context_data(*args,**kwargs)								#Can accept many 
		get_med_form = GetMedForm()
		user  = self.request.user
		print("User------>",user)
		context['get_med_form'] = get_med_form
		return context
		
#Function Method 
def getmed(request):																	#Get for function method
	context = {}
	template_name = "specmed.html"														#will b directed to this
	get_med_form = GetMedForm2(request.POST or None)									#views.py has this class
	lest = "hello world"																#will b printed at HOMEPAGE
	context['text'] = lest																#lest is a variable which stores text 
	print('getmed function')
	context['get_med_form'] = get_med_form												# value get stored in context as get_med_form
	if request.method == 'POST':														#specmed.py <form method >
		print('Hello POsT')																 
		if get_med_form.is_valid():														#to check its correct or not
			item = get_med_form.cleaned_data.get('itemcode')							#value will b stored in item 
			queryset = medicine.objects.filter(ItemCode = item)							#queryset will store the value extracted
			med_name = []
			if queryset:																

				print("Got it")
				for med in queryset:													#loop is created and elements ar
					name = med.Descr
					print(name)
					med_name.append(name)
				return HttpResponse(med_name)											#return a http response
			else:
				print('No such Med')
				return redirect('getmed')
		else:
			print("Error")
			
	return render(request,template_name,context)
