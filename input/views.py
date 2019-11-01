from django.views.generic import CreateView, ListView
from .models import CostOfGood

class InputPage(CreateView):
    model = CostOfGood
    template_name ='create_proposal.html'
    fields = '__all__'

class ResultPage(ListView):
    model = CostOfGood
    template_name = 'result.html'