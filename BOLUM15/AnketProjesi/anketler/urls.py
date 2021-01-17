from django.urls import path

from . import views

app_name = "anketler"


urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    # /anketler/4/
    path('<int:pk>/',views.DetailView.as_view(),name="detay"),
    # /anketler/4/sonuclar/
    path('<int:pk>/sonuclar/',views.ResultView.as_view(),name="sonuclar"),
    # /anketler/4/cevap/
    path('<int:soru_id>/cevap/',views.cevap,name='cevap'),

]


# urlpatterns = [
#     path('',views.index,name='index'),
#     # /anketler/4/
#     path('<int:soru_id>/',views.detay,name="detay"),
#     # /anketler/4/sonuclar/
#     path('<int:soru_id>/sonuclar/',views.sonuclar,name="sonuclar"),
#     # /anketler/4/cevap/
#     path('<int:soru_id>/cevap/',views.cevap,name='cevap'),

# ]
