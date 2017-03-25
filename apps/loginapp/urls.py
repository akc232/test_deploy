from django.conf.urls import url
# from . import views
from views import index, process, login, success, logout
app_name="login"
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^register$', process, name='process'),
    url(r'^login$', login, name='login'),
    url(r'^success$', success, name='success'),
    url(r'^logout$', logout, name='logout'),

]
