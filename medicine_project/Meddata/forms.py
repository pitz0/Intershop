from django import forms
from .models import medicine

class GetMedForm(forms.ModelForm):
	class Meta:
		model = medicine
		fields = ['ItemCode']
	
class GetMedForm2(forms.Form):

	itemcode = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}),required = True)
