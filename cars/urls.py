from django.conf.urls import url
#from django.contrib import admin
from . import views

urlpatterns = [
    #url(r'^admin/', admin.site.urls),

    url(r'^(?P<marka>[\w\-]+)/$', views.home_view, name='home_view'),


]
