from django.contrib import admin
from Meddata.models import *

# Register your models here.

class MedicineAdmin(admin.ModelAdmin):
	list_display = ['Descr','MRP','MFG']
	

	class Meta:
		model  = medicine

admin.site.register(MFG) 
admin.site.register(GENERIC) 
admin.site.register(medicine,MedicineAdmin) 