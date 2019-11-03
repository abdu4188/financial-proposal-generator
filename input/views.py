from django.shortcuts import render
from django.http import HttpResponse
from .forms import createNewFinancial
from .merge import merge

def inputPage(request):

    
    form = createNewFinancial()
    return render(request, 'create_proposal.html', {'form': form})

def resultPage(request):
    if request.method == 'POST':
        form =createNewFinancial(request.POST)
        if form.is_valid():
            name = form.cleaned_data['file_name']
            organization = form.cleaned_data['organization_name']
            project_type = form.cleaned_data['project_type']
            reference = form.cleaned_data['reference_number']
            our_ref_no = form.cleaned_data['our_reference_number']
            date = form.cleaned_data['date']
            item_no = form.cleaned_data['item_no']
            part_no = form.cleaned_data['part_no']
            description = form.cleaned_data['description']
            quantity = form.cleaned_data['quantity']
            unit_market_price = form.cleaned_data['unit_market_price']
            markup_percentage = form.cleaned_data['markup_percentage']
            
            merge(name, organization, project_type, reference, our_ref_no, date, item_no, part_no, description, quantity, unit_market_price, markup_percentage)

    return render(request, 'result.html')