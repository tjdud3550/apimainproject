
from django.contrib import admin
from django.conf.urls import url,include
from django.urls import path
from rest_framework import routers 
from movies.views import MovieViewSet

router = routers.DefaultRouter()
router.register('movies',MovieViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^admin/', admin.site.urls), 
    url(r'^',include(router.urls)),

]
