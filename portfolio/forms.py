from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'u-border-1 u-border-grey-30 u-input u-input-rectangle u-white',
        'placeholder': 'Enter your name',
        'id': 'name-3b9a',
        'required': True
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'u-border-1 u-border-grey-30 u-input u-input-rectangle u-white',
        'placeholder': 'Enter a valid email address',
        'id': 'email-3b9a',
        'required': True
    }))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'u-border-1 u-border-grey-30 u-input u-input-rectangle u-white',
        'placeholder': 'Enter your phone number',
        'id': 'phone-d78d',
        'required': True
    }))
    subject = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'u-border-1 u-border-grey-30 u-input u-input-rectangle u-white',
        'placeholder': 'Enter subject',
        'id': 'text-9800',
        'required': True
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 4,
        'cols': 50,
        'class': 'u-border-1 u-border-grey-30 u-input u-input-rectangle u-white',
        'placeholder': 'Enter your message',
        'id': 'message-3b9a',
        'required': True
    }))

    class Meta:
        model = Contact
        fields = '__all__'
        labels = {
            'name': 'Name',
            'email': 'Email',
            'phone_number': 'Number',
            'subject': 'Subject',
            'message': 'Message'
        }

