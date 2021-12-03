from django.db import models

# Create your models here.
class Drug(models.Model) :
    drugname = models.CharField(max_length=30, default='')
    isopioid = models.CharField(max_length=5)

    class Meta:
        db_table = 'pd_drugs'
    
    def __str__(self) :
        return self.drugname

class Prescriber(models.Model):
    fname = models.CharField(max_length=11, blank=False)
    lname = models.CharField(max_length=11, blank=False)
    gender = models.CharField(max_length=1, blank=False)
    state = models.CharField(max_length=2, blank=False)
    credentials = models.CharField(max_length=20, blank=True)
    specialty = models.CharField(max_length=62, blank=False)
    isopioidprescriber = models.BooleanField(default=False)
    totalprescriptions = models.IntegerField(blank=False)

    class Meta:
        db_table = "pd_Prescriber"
    

    
    def __str__(self):
        return (self.fname)
