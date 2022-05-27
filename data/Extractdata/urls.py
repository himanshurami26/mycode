from django.urls import path, include
from Extractdata.views import DataView,expostdataindb

urlpatterns = [
    path('data', DataView.as_view(), name='data'),
    path('postdata', expostdataindb.as_view() , name='register')
]