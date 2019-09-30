from firstapp import views
from django.conf.urls import url

app_name='firstapp'
urlpatterns = [

    url(r'^about/$', views.about,name="about"),
    url(r'^base/$',views.index1,name="base"),
    url(r'^form/$',views.index2),
    url(r'^pd/$',views.updatefunction),
    url(r'^fetch/$',views.datafetch),
    url(r'^delete/$',views.deletedata),
    url(r'^edit/$',views.editdata)
]