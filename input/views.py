from django.shortcuts import render
from django.http import HttpResponse
from .forms import createNewFinancial
from .merge import merge
import json
from django.http import JsonResponse

def inputPage(request):
    
    form = createNewFinancial()
    return render(request, 'create_proposal.html', {'form': form})

def resultPage(request):
    
    jsonData = request.GET.get('values')
    generalData = request.GET.get('general')
    jsonData = json.loads(jsonData)
    generalData = json.loads(generalData)
    
    merge(jsonData, generalData)
    return JsonResponse("Document written successfully", safe=False)


    # return render(request, 'result.html')