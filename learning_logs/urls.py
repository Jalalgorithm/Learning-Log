"""Define url patterns for the learning logs"""

from django.urls import path

from . import views

app_name = 'learning_logs'

urlpatterns=[
    #Home page
    path('' , views.index , name='index'),
    
    #Topics Page 
    path('topics/' , views.topics , name='topics'),
    
    #Details page for a single topic
    path('topics/<int:topic_id>/' , views.topic , name='topic'),
    
    path('new_topic/' , views.new_topic , name='new_topic')
    
    
]