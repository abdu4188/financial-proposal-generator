from mailmerge import MailMerge
from .unit_price import calculateUitPrice
from django.http import JsonResponse
from .models import Record
from datetime import datetime

def merge(jsonData, generalData):

    name = generalData['file_name']
    organization = generalData['organization_name']
    project_type = generalData['project_type']
    reference = generalData['reference_number']
    our_reference = generalData['our_reference_number']
    date = generalData['date']
    datetimeobject = datetime.strptime(date,'%m/%d/%Y')
    date = datetimeobject.strftime('%B %d, %Y')
    exchange_rate = generalData['exchange_rate']
    notes = generalData['notes']

    unit_market_price = []
    markup_percentage = []
    item_no = []
    part_no = []
    description = []
    quantity = []
    total = 0

    for i in range(len(jsonData)):
        ump = float(jsonData[i]['unit_market_price']) * float(exchange_rate)
        unit_market_price.append(ump)
        markup_percentage.append(jsonData[i]['markup_percentage'])
        item_no.append(jsonData[i]['item_no'])
        part_no.append(jsonData[i]['part_no'])
        description.append(jsonData[i]['description'])
        quantity.append(jsonData[i]['quantity'])


    for i in range(len(jsonData)):
        total = total + (calculateUitPrice(float(unit_market_price[i]),float(markup_percentage[i])) * float(quantity[i]))
        
    total= str(total)
    

    template = 'master.docx'
    document = MailMerge(template)

    document.merge(
        organization = organization,
        project_type = project_type, 
        reference = reference,
        our_ref_no = our_reference,
        date = date,
        notes = notes,
        total = total,
    )
    item_table = [
    {
        'item_no' : str(data['item_no']),
        'part_no' : str(data['part_no']),
        'description' : str(data['description']),
        'quantity' : str(data['quantity']),
        'unit_price' : str(calculateUitPrice(
            (float(data['unit_market_price']) * float(exchange_rate)),
            float(data['markup_percentage']))
        ),
        'total_price' : str(calculateUitPrice(
            (float(data['unit_market_price']) * float(exchange_rate)),
            float(data['markup_percentage'])) * float(data['quantity']))  
    } 
    for data in jsonData
]


    document.merge_rows('item_no', item_table)
    document.write('documents/'+name+'.docx')

    now = datetime.now()
    # dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    record = Record(path = name+'.docx', date = now, organization = organization, project_type = project_type)
    record.save()

    return

