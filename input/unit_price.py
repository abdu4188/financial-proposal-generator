from.models import ConstantField

def calculateUitPrice(unit_market_price, markup_percentage):
    all_objects = ConstantField.objects.all()[0]
    cifValue = unit_market_price + all_objects.freightAndInsurance + all_objects.otherCosts
    customsDuty = cifValue * (all_objects.customsRate)/100
    exciseTax = (cifValue + customsDuty) * (all_objects.exciseTax)/100
    afterExicseTax = cifValue + customsDuty + exciseTax
    afterVat = afterExicseTax + (afterExicseTax * all_objects.vat)
    afterSurtax = afterVat + (afterVat * all_objects.surtax)
    withHoldingTax = cifValue * (all_objects.withholdingTax)/100
    costOfGoods = afterSurtax + withHoldingTax
    unitSalesPrice = costOfGoods + (costOfGoods * (markup_percentage/100))
    
    return unitSalesPrice