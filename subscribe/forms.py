from django import forms
from django.utils.translation import gettext_lazy as _
from subscribe.models import Subscribe


# class SubscribeForm(forms.Form):
#   first_name = forms.CharField(max_length=100)
#   last_name = forms.CharField(max_length=100)
#   email = forms.EmailField(max_length=100)

class SubscribeForm(forms.ModelForm):
  class Meta:
    model = Subscribe
    fields ='__all__'
    labels = {
      'first_name': _('Enter first name'),
    }
    error_messages = {
      'first_name' : {
        'required': _('you have to fill the first name')
      }
    }