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

	ItemCode = models.CharField(max_length=60,null  = True)                             #these are the container for our data type
	MFG = models.CharField(max_length=60,null  = True)                                  
	Descr = models.CharField(max_length=60,null  = True)
	EntryDt = models.DateTimeField(null  = True)
	GnCode = models.CharField(max_length=60,null  = True)
	generic_med = models.ForeignKey(GENERIC, on_delete = models.CASCADE, null =True)
	PACK = models.CharField(max_length=60,null  = True)
	STRENGTH = models.CharField(max_length=60,null  = True)
	CATEGORY = models.CharField(max_length=60,null  = True)
	MfgCode = models.CharField(max_length=60,null  = True)
	mfg = models.ForeignKey("MFG", on_delete = models.CASCADE, null  = True)
	HPRate = models.DecimalField(max_digits=19, decimal_places=2,null  = True)
	Rate = models.DecimalField(max_digits=19, decimal_places=2,null  = True)
	MRP = models.DecimalField(max_digits=19, decimal_places=2,null  = True)
	HMARGIN = models.DecimalField(max_digits=19, decimal_places=2,null  = True)
	RMARGIN = models.DecimalField(max_digits=19, decimal_places=2,null  = True)
	TAX = models.DecimalField(max_digits=19, decimal_places=2,null  = True)
	MST = models.DecimalField(max_digits=19, decimal_places=2,null  = True)
	CST = models.DecimalField(max_digits=19, decimal_places=2,null  = True)
	OCT = models.DecimalField(max_digits=19, decimal_places=2,null  = True)
	EXICE = models.DecimalField(max_digits=19, decimal_places=2,null  = True)
	PIS = models.CharField(max_length=60,null  = True)
	PISNO = models.CharField(max_length=60,null  = True)
	PISDATE = models.DateTimeField(null = True)

	def __str__(self):
		return "{}"-"{}".format(self.Descr, self.ItemCode)