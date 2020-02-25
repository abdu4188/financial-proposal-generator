from django import forms
from bootstrap_datepicker_plus import DatePickerInput
from django.db import models
from datetime import datetime
class createNewFinancial(forms.Form):
    file_name = forms.CharField(widget= forms.TextInput(attrs ={'class': 'form-control'}))
    organization_name = forms.CharField(widget= forms.TextInput(attrs ={'class': 'form-control'}))
    project_type = forms.CharField(widget= forms.TextInput(attrs ={'class': 'form-control'}))
    reference_number = forms.CharField(widget= forms.TextInput(attrs ={'class': 'form-control'}))
    our_reference_number = forms.CharField(widget= forms.TextInput(attrs ={'class': 'form-control'}))
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%m/%d/%Y")
    date = forms.DateField(
        required = True,
        widget=DatePickerInput(format='%m/%d/%Y', attrs={'required': 'required', 'value': timestampStr})
    )
    item_no = forms.FloatField(widget= forms.TextInput(attrs ={'class': 'form-control', 'type': 'number'}))
    part_no = forms.CharField(widget= forms.TextInput(attrs ={'class': 'form-control'}))
    description = forms.CharField(widget= forms.TextInput(attrs ={'class': 'form-control'}))
    quantity = forms.FloatField(widget= forms.TextInput(attrs ={'class': 'form-control', 'type': 'number'}))
    unit_market_price = forms.FloatField(widget= forms.TextInput(attrs ={'class': 'form-control', 'type': 'number'}))
    markup_percentage = forms.FloatField(widget= forms.TextInput(attrs ={'class': 'form-control', 'type': 'number'}))
    exchange_rate = forms.FloatField(widget = forms.TextInput(attrs={'class': 'form-control', 'type': 'number', 'step': '0.01', 'value': '0',}), initial = 1)
    notes = forms.CharField(widget = forms.Textarea(attrs ={'class': 'form-control'}))
    NOTES_OPTIONS = (
        ('0', 'Please add 15% VAT'),
        ('1', 'Price is valid for 45 days'),
        ('2', 'All price is in Ethiopian Birr'),
        ('3', 'Delivery will be within 45 days after PO, advance and bank foreign currency approval'),
        ('4', 'Payment Term 50% advance and remaining amount after delivery'),
        ('5', 'Installation is NOT part of this Quote'),
        ('6', 'If there is discrepancy in price calculation the unit price will prevail')
    )
    note_choices = forms.MultipleChoiceField(required = False, widget = forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}), choices = NOTES_OPTIONS)