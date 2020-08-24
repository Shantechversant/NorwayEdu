from django.urls import path, include
from apis import views as api_views 

urlpatterns = [
    path('user', api_views.Users.as_view(), name='user')
]
