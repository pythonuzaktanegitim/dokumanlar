from django import forms

class IletisimForm(forms.Form):
    kimden = forms.EmailField(required=True)
    konu = forms.CharField(required=True)
    mesaj = forms.CharField(widget=forms.Textarea,required=True)
