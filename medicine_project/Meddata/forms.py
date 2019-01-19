from django.forms import ModelForm
from .models import medicine

class GetMedForm(ModelForm):
	class Meta:
		model = medicine
		fields = ['ItemCode']



