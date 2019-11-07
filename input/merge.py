from mailmerge import MailMerge
from .unit_price import calculateUitPrice
from django.http import JsonResponse

def merge(jsonData, generalData):

    name = generalData['file_name']
    organization = generalData['organization_name']
    project_type = generalData['project_type']
    reference = generalData['reference_number']
    our_reference = generalData['our_reference_number']
    date = generalData['date']

    unit_market_price = []
    markup_percentage = []
    item_no = []
    part_no = []
    description = []
    quantity = []

    for i in range(len(jsonData)) :
        unit_market_price.append(jsonData[i]['unit_market_price'])
        markup_percentage.append(jsonData[i]['markup_percentage'])
        item_no.append(jsonData[i]['item_no'])
        part_no.append(jsonData[i]['part_no'])
        description.append(jsonData[i]['description'])
        quantity.append(jsonData[i]['quantity'])


    

    template = 'master.docx'
    document = MailMerge(template)

    document.merge(
        organization = organization,
        project_type = project_type, 
        reference = reference,
        our_ref_no = our_reference,
        date = date,
    )
    item_table = [
    {
        'item_no' : str(data['item_no']),
        'part_no' : str(data['part_no']),
        'description' : str(data['description']),
        'quantity' : str(data['quantity']),
        'unit_price' : str(calculateUitPrice(
            float(data['unit_market_price']),
            float(data['markup_percentage']))
        ),
        'total_price' : str(calculateUitPrice(
            float(data['unit_market_price']),
            float(data['markup_percentage'])) * float(data['quantity']))  
    } 
    for data in jsonData
]


    document.merge_rows('item_no', item_table)
    document.write('documents/'+name+'.docx')

    return JsonResponse("Document written successfully")
