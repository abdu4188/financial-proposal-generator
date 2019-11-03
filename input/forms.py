from django import forms

class createNewFinancial(forms.Form):
    file_name = forms.CharField(widget= forms.TextInput(attrs ={'class': 'form-control'}))
    organization_name = forms.CharField(widget= forms.TextInput(attrs ={'class': 'form-control'}))
    project_type = forms.CharField(widget= forms.TextInput(attrs ={'class': 'form-control'}))
    reference_number = forms.CharField(widget= forms.TextInput(attrs ={'class': 'form-control'}))
    our_reference_number = forms.CharField(widget= forms.TextInput(attrs ={'class': 'form-control'}))
    date = forms.CharField(widget= forms.TextInput(attrs ={'class': 'form-control'}))
    item_no = forms.FloatField(widget= forms.TextInput(attrs ={'class': 'form-control', 'type': 'number'}))
    part_no = forms.CharField(widget= forms.TextInput(attrs ={'class': 'form-control'}))
    description = forms.CharField(widget= forms.TextInput(attrs ={'class': 'form-control'}))
    quantity = forms.FloatField(widget= forms.TextInput(attrs ={'class': 'form-control', 'type': 'number'}))
    unit_market_price = forms.FloatField(widget= forms.TextInput(attrs ={'class': 'form-control', 'type': 'number'}))
    markup_percentage = forms.FloatField(widget= forms.TextInput(attrs ={'class': 'form-control', 'type': 'number'}))
