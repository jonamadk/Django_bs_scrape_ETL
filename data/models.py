from django.db import models

# Create your models here.
 

class LiveTradingData(models.Model):
    
    company_name_symbol = models.CharField(max_length= 20, null = True)
    high_value = models.FloatField(blank= True, null= True)
    low_value = models.FloatField(blank = True, null= True)
    open_value = models.FloatField(blank= True, null = True)
    qty = models.FloatField(blank = True, null = True)
    change_percent_value = models.FloatField(blank = True, null = True)
    date_value = models.CharField(max_length =40,null=True)


    class Meta:
        verbose_name ="LiveTradingData"
    

    def __str__(self):
        return self.company_name_symbol 

    def __unicode__(self):
        return  self.company_name_symbol

# class TableData(models.Model):
#     published_date = models.DateField(auto_now_add=True, blank=True, null=True)


