from django.db import models
from django.utils.translation import gettext_lazy as _

class pemasukan(models.Model):
    nama = models.CharField(max_length=255)
    jumlah = models.IntegerField()
    tanggal = models.DateField('%d-%m-%y')

    class Meta:
        db_table = 'pemasukan'


class pengeluaran(models.Model):
    nama = models.CharField(max_length=255)
    jumlah = models.IntegerField()
    tanggal = models.DateField()

    class Meta:
        db_table = 'pengeluaran'



  

