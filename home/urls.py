from django.urls import path
from django.conf.urls import url,include
from home import views
urlpatterns = [
    path('',views.home),
    path('show',views.show),
    path('send',views.send),
    path('delete',views.delete),
    path('edit',views.edit),
    path('recordedit',views.recordedit),
]


