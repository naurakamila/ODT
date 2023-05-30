from django import forms
from django.utils.translation import gettext_lazy as _
from .models import pemasukan, pengeluaran

class pemasukanForm(forms.ModelForm):
    class Meta:
        model = pemasukan
        fields = ['nama', 'jumlah', 'tanggal']
        labels = {
            'nama': _('Nama & Keterangan'),
            'jumlah' : _('Jumlah'),
            'tanggal' : _('Tanggal')
        }
     
class pengeluaranForm(forms.ModelForm):
    class Meta:
        model = pengeluaran
        fields = ['nama', 'jumlah', 'tanggal']
        labels = {
            'nama': _('Nama & Keterangan'),
            'jumlah' : _('Jumlah'),
            'tanggal' : _('Tanggal')
        }

 