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
    
    note =[]
    note.append('Please add 15% VAT')
    note.append('Price is valid for 45 days')
    note.append('All price is in Ethiopian Birr')
    note.append('Delivery will be within 45 days after PO, advance and bank foreign currency approval')
    note.append('Payment Term 50% advance and remaining amount after delivery')
    note.append('Installation is NOT part of this Quote')
    note.append('If there is discrepancy in price calculation the unit price will prevail')

    selectedNotes = []
    for x in generalData['vat']:
        selectedNotes.append(int(x))
    
    temp = [0,1,2,3,4,5,6]
    for selected in selectedNotes:
        temp[selected]= ''
    
    temp_note = ['','','','','','','']    
    
    for y in [0,1,2,3,4,5,6]:
        if temp[y] == '':
            temp_note[y] = note[y]
                
    for elem in temp_note:
        if elem == '':
            temp_note.remove(elem)

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

    reminder_table=[
        {
            'reminder': temp_reminder
        }
        for temp_reminder in temp_note
    ]

    document.merge_rows('item_no', item_table)
    document.merge_rows('reminder', reminder_table)
    document.write('documents/'+name+'.docx')

    now = datetime.now()

    record = Record(path = name+'.docx', date = now, organization = organization, project_type = project_type)
    record.save()

    return

