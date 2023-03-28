from django import forms


class Productform(forms.Form):
    name=forms.CharField(label="Product Name",max_length=50)
    price=forms.IntegerField(label="Product price",max_value=50000)
    email=forms.EmailField(label="Company Email",required=False)
