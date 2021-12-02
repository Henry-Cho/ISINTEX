from django.db import models

# Create your models here.
class Drug(models.Model) :
    drugname = models.CharField(max_length=30, default='')
    isopioid = models.BooleanField(default=False)

    class Meta:
        db_table = 'pd_drugs'
    
    def __str__(self) :
        return self.drugname