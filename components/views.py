from django.shortcuts import redirect, render,  get_object_or_404

from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import Http404
from .forms import pemasukanForm, pengeluaranForm
from .models import pemasukan, pengeluaran

def in_view(request):
    pemasukan = pemasukan.objects.all()
    
    context = {
        'pemasukan' : pemasukan
    }
    return render(request, 'components/tables-datatable.html', context)


def out_view(request):
    pengeluaran = pengeluaran.objects.all()
    
    context = {
        'pengeluaran' : pengeluaran
    }
    return render(request, 'components/tables-basic.html', context)

def form_in(request):
    if request.method == 'POST':
        form = pemasukanForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('tables_datatable')
    else:
        form = pemasukanForm()
    
    return render(request, 'components/forms/form-validation.html', {'form': form})

def form_out(request):
    if request.method == 'POST':
        form = pengeluaranForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('tables_basic')
    else:
        form = pengeluaranForm()
    
    return render(request, 'components/forms/form-editors.html', {'form': form})

# Membuat View untuk menghapus data task
def delete_view(request, item_id):
    try:
        task = pemasukan.objects.get(pk=item_id)
        task.delete()
        messages.success(request, 'Sukses Menghapus Data')
        return redirect('tables_datatable')
    except pemasukan.DoesNotExist:
        raise Http404("Data tidak ditemukan.")

def delete_view2(request, item_id):
    try:
        task = pengeluaran.objects.get(pk=item_id)
        task.delete()
        messages.success(request, 'Sukses Menghapus Data')
        return redirect('tables_basic')
    except pengeluaran.DoesNotExist:
        raise Http404("Data tidak ditemukan.")

############ Components ############
# UI Elements 
class Alerts(LoginRequiredMixin,TemplateView):
    template_name = "components/ui_elements/ui-alerts.html"
class Buttons(LoginRequiredMixin,TemplateView):
    template_name = "components/ui_elements/ui-buttons.html"
class Cards(LoginRequiredMixin,TemplateView):
    template_name = "components/ui_elements/ui-cards.html"
class Carousel(LoginRequiredMixin,TemplateView):
    template_name = "components/ui_elements/ui-carousel.html"
class Colors(LoginRequiredMixin,TemplateView):
    template_name = "components/ui_elements/ui-colors.html"
class Dropdowns(LoginRequiredMixin,TemplateView):
    template_name = "components/ui_elements/ui-dropdowns.html"
class Generals(LoginRequiredMixin,TemplateView):
    template_name = "components/ui_elements/ui-general.html"
class Grid(LoginRequiredMixin,TemplateView):
    template_name = "components/ui_elements/ui-grid.html"
class Images(LoginRequiredMixin,TemplateView):
    template_name = "components/ui_elements/ui-images.html"
class Lightbox(LoginRequiredMixin,TemplateView):
    template_name = "components/ui_elements/ui-lightbox.html"
class Modals(LoginRequiredMixin,TemplateView):
    template_name = "components/ui_elements/ui-modals.html"
class Progressbars(LoginRequiredMixin,TemplateView):
    template_name = "components/ui_elements/ui-progressbars.html"
class Rangeslider(LoginRequiredMixin,TemplateView):
    template_name = "components/ui_elements/ui-rangeslider.html"
class Rating(LoginRequiredMixin,TemplateView):
    template_name = "components/ui_elements/ui-rating.html"
class SessionTimeout(LoginRequiredMixin,TemplateView):
    template_name = "components/ui_elements/ui-session-timeout.html"
class SweetAlert(LoginRequiredMixin,TemplateView):
    template_name = "components/ui_elements/ui-sweet-alert.html"
class TabsAccordions(LoginRequiredMixin,TemplateView):
    template_name = "components/ui_elements/ui-tabs-accordions.html"
class Typography(LoginRequiredMixin,TemplateView):
    template_name = "components/ui_elements/ui-typography.html"
class Video(LoginRequiredMixin,TemplateView):
    template_name = "components/ui_elements/ui-video.html"

# Forms
class Elements(LoginRequiredMixin,TemplateView):
    template_name = "components/forms/form-elements.html"
class Validation(LoginRequiredMixin,TemplateView):
    template_name = "components/forms/form-validation.html"
    
    
class Advanced(LoginRequiredMixin,TemplateView):
    template_name = "components/forms/form-advanced.html"
class Editors(LoginRequiredMixin,TemplateView):
    template_name = "components/forms/form-editors.html"
class Upload(LoginRequiredMixin,TemplateView):
    template_name = "components/forms/form-uploads.html"
class Xeditable(LoginRequiredMixin,TemplateView):
    template_name = "components/forms/form-xeditable.html"
class Wizard(LoginRequiredMixin,TemplateView):
    template_name = "components/forms/form-wizard.html"
class Mask(LoginRequiredMixin,TemplateView):
    template_name = "components/forms/form-mask.html"

# Charts
class Apex(LoginRequiredMixin,TemplateView):
    template_name = "components/charts/charts-apex.html"
class Chartist(LoginRequiredMixin,TemplateView):
    template_name = "components/charts/charts-chartist.html"
class Chartjs(LoginRequiredMixin,TemplateView):
    template_name = "components/charts/charts-chartjs.html"
class Flot(LoginRequiredMixin,TemplateView):
    template_name = "components/charts/charts-flot.html"
class Knob(LoginRequiredMixin,TemplateView):
    template_name = "components/charts/charts-knob.html"
class Sparkline(LoginRequiredMixin,TemplateView):
    template_name = "components/charts/charts-sparkline.html"

# Tables
class Basic(LoginRequiredMixin,TemplateView):
    template_name = "components/tables/tables-basic.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['pengeluaran'] = pengeluaran.objects.all()
        
        return context
class Datatable(LoginRequiredMixin,TemplateView):
    template_name = "components/tables/tables-datatable.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['pemasukan'] = pemasukan.objects.all()
        
        return context

class Editable(LoginRequiredMixin,TemplateView):
    template_name = "components/tables/tables-editable.html"
class Responsive(LoginRequiredMixin,TemplateView):
    template_name = "components/tables/tables-responsive.html"

# Icons
class Dripicons(LoginRequiredMixin,TemplateView):
    template_name = "components/icons/icons-dripicons.html"
class Fontawesome(LoginRequiredMixin,TemplateView):
    template_name = "components/icons/icons-fontawesome.html"
class Materialdesign(LoginRequiredMixin,TemplateView):
    template_name = "components/icons/icons-materialdesign.html"
class Themify(LoginRequiredMixin,TemplateView):
    template_name = "components/icons/icons-themify.html"

# Maps
class Google(LoginRequiredMixin,TemplateView):
    template_name = "components/maps/maps-google.html"
class Vector(LoginRequiredMixin,TemplateView):
    template_name = "components/maps/maps-vector.html"