from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Sorular

class SoruModelTest(TestCase):
    def test_sonrası_sorular(self):
        zaman = timezone.now() + datetime.timedelta(days=30)
        gelecek_soru = Sorular(yayim_zaman=zaman)
        self.assertIs(gelecek_soru.son_zaman_sorular(),False)
