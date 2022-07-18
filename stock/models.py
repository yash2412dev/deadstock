from pickle import TRUE
from django.db import models
from django.urls import reverse
# Create your models here.

class inventory(models.Model):
   
    Sr_no = models.AutoField(primary_key=True)
    Dsr_no = models.CharField(max_length=250)
    Voucher_no = models.CharField(max_length=250)
    Recipt_date = models.DateField()
    supplier_name_adress = models.CharField(max_length=500)
    rv_no = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    qty_recived = models.IntegerField()
    qty_issued = models.IntegerField()
    qty_balanced = models.IntegerField()
    cost = models.IntegerField()
    current_locaton = models.CharField(max_length=20)
    depriciation_cost = models.IntegerField()
    def get_absolute_url(self):
        return reverse('stock:inventory_detail',
                       args=[self.Sr_no,
                             self.Dsr_no,
                             self.Voucher_no,
                             self.Recipt_date])

