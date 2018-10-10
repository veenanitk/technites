from django.conf.urls import url
from polls import views
app_name = "polls"

urlpatterns = [
   
    url(r'^main_page/', views.main_page, name='main_page'),
]