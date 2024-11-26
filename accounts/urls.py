from django.urls import path , include


aap_name='accounts'

urlpatterns =[
    path('' , include('django.contrib.auth.urls')),
]