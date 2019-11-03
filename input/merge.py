from __future__ import print_function
from mailmerge import MailMerge
from .unit_price import calculateUitPrice

def merge(name, organization, project_type, reference, our_reference, date, item_no, part_no, description, quantity, unit_market_price, markup_percentage):
    template = 'master.docx'
    document = MailMerge(template)

    unit_price = calculateUitPrice(unit_market_price, markup_percentage)
    total_price = quantity * unit_price

    document.merge(
        organization = organization,
        project_type = project_type, 
        reference = reference,
        our_ref_no = our_reference,
        date = date,
    )
    item_table = [{
        'item_no' : str(item_no),
        'part_no' : str(part_no),
        'description' : str(description),
        'quantity' : str(quantity),
        'unit_price' : str(unit_price),
        'total_price' : str(total_price)
    },{
        'item_no' : str(item_no),
        'part_no' : str(part_no),
        'description' : str(description),
        'quantity' : str(quantity),
        'unit_price' : str(unit_price),
        'total_price' : str(total_price)
    }
    ]

    document.merge_rows('item_no', item_table)
    document.write(name+'.docx')
