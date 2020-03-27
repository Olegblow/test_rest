from django.urls import include
from django.urls import path
from rest_framework import routers

from .views import ApplicationSet
from .views import Test
from .views import UpdateApikey

from rest_framework.authtoken import views


router = routers.DefaultRouter()


urlpatterns = [
    path('api/', include([
        path('apikey/create/', ApplicationSet.as_view(), name='create_api_key'),
        path('apikey/update/<int:pk>/',
             UpdateApikey.as_view(), name='update_api_key'),
        path('test/<str:api_key>/', Test.as_view(), name='api_test'),
    ])),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework')),
    path('api-token-auth/', views.obtain_auth_token),
    path('djoser-auth/', include('djoser.urls')),
    path('djoser-auth/', include('djoser.urls.authtoken')),
]
