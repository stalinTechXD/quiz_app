from django import forms
from odessy.models import ody
from odessy.models import hell
from odessy.models import od

class yep(forms.ModelForm):
    class Meta:
        model = ody
        fields = '__all__'



class p(forms.ModelForm):
    class Meta:
        model = hell
        fields = '__all__'



class ll(forms.ModelForm):
    class Meta:
        model = od
        fields = '__all__'        
         
 