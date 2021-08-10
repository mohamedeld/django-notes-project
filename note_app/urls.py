from django.conf.urls import url
from . import views

app_name = 'note_app'
urlpatterns=[
    url(r'^$',views.all_notes,name='all_notes'),
    url(r'^(?P<slug>[-\w]+)/$',views.note_detail,name='note_detail'),
    url(r'^add$',views.create_note,name='create_note'),
    url(r'^(?P<slug>[-\w]+)/edit$',views.edit_note,name='edit_note'),

    ]
