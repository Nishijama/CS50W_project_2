from django import forms
from .models import Listing

categories=[
    ('', 'Choose category'),
    ('sport', 'Sport'),
    ('fashion', 'Fashion'),
    ('toys', 'Toys'),
    ('electronics', 'Electronics'),
    ('home', 'Home'),
    ('cars', 'Cars'),
    ('art', 'Art'),
    ('other', 'Other')
]

class NewListingForm(forms.ModelForm):

    class Meta:
        model = Listing
        fields = ('title','price', 'category','end_date','item_image', 'description')
        widgets = {
            'category': forms.Select(choices=categories),
            'description': forms.Textarea,
            'price': forms.NumberInput(attrs={'min':0}),
            }