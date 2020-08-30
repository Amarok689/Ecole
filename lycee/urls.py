  
from django.conf.urls import url
from . import views
from django.urls import path
from .views import StudentCreateView, ParticularCreateView, StudentEditView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<cursus_id>[0-9]+)$', views.detail, name='detail'),
    # /lycee/student/73
    url(r'^student/(?P<student_id>[0-9]+)$', views.detail_student, name='detail_student'),
    url(r'^student/create/$', StudentCreateView.as_view(), name='create_student'),
    url(r'^form/particular/$', ParticularCreateView.as_view(), name='particular'),
    url(r'^form/edition/(?P<pk>\d+)$', StudentEditView.as_view(), name='edition'),
    url(r'^form/(?P<student_id>[0-9]+)$', views.Callofroll, name='callofroll')
    ]