from django.forms import ModelForm
from .models import Yazar

class YazarForm(ModelForm):

    class Meta:
        model = Yazar
        fields = ('adi','soyadi','dogum_tarihi')
        labels = {
            'adi':"Adı",
            'soyadi':"Soyadı",
            'dogum_tarihi':"Doğum Tarihi"
        }
        help_texts = {
            'dogum_tarihi':"Her Sanatçı Ölümsüzdür."
        } 