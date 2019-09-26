from django import forms
from .models import Rating


class RatingForm(forms.Form):

    # # def MyForm(forms.Form):
    #def __init__(self, *args, **kwargs):
     #   super(RatingForm, self).__init__(*args, **kwargs)
        #self.fields['li'].label = False
        #kwargs.setdefault('li','')



    rating = forms.ChoiceField(choices=Rating.rvalues, widget=forms.RadioSelect())

# class RatingForm(forms.Form):
#     class Meta:
#         model = Rating
#         fields = ['rating']
