from django.views.generic import CreateView
from .models import

class InputPage(CreateView):
    template_name ='create_proposal.html'