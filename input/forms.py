from django import forms
from bootstrap_datepicker_plus import DatePickerInput
class createNewFinancial(forms.Form):
    file_name = forms.CharField(widget= forms.TextInput(attrs ={'class': 'form-control'}))
    organization_name = forms.CharField(widget= forms.TextInput(attrs ={'class': 'form-control'}))
    project_type = forms.CharField(widget= forms.TextInput(attrs ={'class': 'form-control'}))
    reference_number = forms.CharField(widget= forms.TextInput(attrs ={'class': 'form-control'}))
    our_reference_number = forms.CharField(widget= forms.TextInput(attrs ={'class': 'form-control'}))
    date = forms.DateField(
        required = True,
        widget=DatePickerInput(format='%m/%d/%Y')
    )
    item_no = forms.FloatField(widget= forms.TextInput(attrs ={'class': 'form-control', 'type': 'number'}))
    part_no = forms.CharField(widget= forms.TextInput(attrs ={'class': 'form-control'}))
    description = forms.CharField(widget= forms.TextInput(attrs ={'class': 'form-control'}))
    quantity = forms.FloatField(widget= forms.TextInput(attrs ={'class': 'form-control', 'type': 'number'}))
    unit_market_price = forms.FloatField(widget= forms.TextInput(attrs ={'class': 'form-control', 'type': 'number'}))
    markup_percentage = forms.FloatField(widget= forms.TextInput(attrs ={'class': 'form-control', 'type': 'number'}))
    exchange_rate = forms.FloatField(widget = forms.TextInput(attrs={'class': 'form-control', 'type': 'number', 'step': '0.01', 'value': '0',}), initial = 0)
    notes = forms.CharField(widget = forms.Textarea(attrs ={'class': 'form-control'}))