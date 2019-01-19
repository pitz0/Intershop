from django.shortcuts import render
from rest_framework import generics
from .models import medicine
from .serializers import MedicineSerializer
from django.views.generic.base import View,TemplateView
from .forms import GetMedForm

# Create your views here.

class ListMedicineView(generics.ListAPIView):
	#providea get method handler
	queryset = medicine.objects.all()
	serializer_class = MedicineSerializer

def home(request):
	return render (request , 'home.html',context = {'key':value})


def landing(request):
	context = {}
	template_name = 'landing.html'
	context['user'] = request.user
	return render(request,template_name,context)


class SpecMedView(TemplateView):
	template_name =  'specmed.html'
	def post(self,request,*args,**kwargs):
		pass
	def get_context_data(self,*args,**kwargs):
		context = super().get_context_data(*args,**kwargs)
		get_med_form = GetMedForm()
		context['get_med_form'] = get_med_form
		return context