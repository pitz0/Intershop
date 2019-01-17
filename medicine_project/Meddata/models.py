from django.db import models

# Create your models here.
class MFG(models.Model):
	COCD = models.CharField(max_length=60)
	NAME = models.CharField(max_length=60)
	SHRTNM = models.CharField(max_length=60)
	Address = models.CharField(max_length=60)
	Phone = models.CharField(max_length=60)
	def __str__(self):
		return self.NAME

class GENERIC(models.Model):
	GDESC = models.CharField(max_length=100)
	GnCode = models.CharField(max_length=60)
	
class medicine(models.Model):

	ItemCode = models.CharField(max_length=60)                             #these are the container for our data type
	MFG = models.CharField(max_length=60)                                  
	Descr = models.CharField(max_length=60)
	EntryDt = models.DateTimeField(null = True)
	GnCode = models.CharField(max_length=60)
	genric_med = models.ForeignKey('GENERIC', on_delete = models.CASCADE, null =True)
	PACK = models.CharField(max_length=60)
	STRENGTH = models.CharField(max_length=60)
	CATEGORY = models.CharField(max_length=60)
	MfgCode = models.CharField(max_length=60)
	mfg = models.ForeignKey("MFG", on_delete = models.CASCADE, null  = True)
	HPRate = models.DecimalField(max_digits=19, decimal_places=2)
	Rate = models.DecimalField(max_digits=19, decimal_places=2)
	MRP = models.DecimalField(max_digits=19, decimal_places=2)
	HMARGIN = models.DecimalField(max_digits=19, decimal_places=2)
	RMARGIN = models.DecimalField(max_digits=19, decimal_places=2)
	TAX = models.DecimalField(max_digits=19, decimal_places=2)
	MST = models.DecimalField(max_digits=19, decimal_places=2)
	CST = models.DecimalField(max_digits=19, decimal_places=2)
	OCT = models.DecimalField(max_digits=19, decimal_places=2)
	EXICE = models.DecimalField(max_digits=19, decimal_places=2)
	PIS = models.CharField(max_length=60)
	PISNO = models.CharField(max_length=60)
	PISDATE = models.DateTimeField(null = True)

	def __str__(self):
		return self.Descr