from django.urls import include, path
from rest_framework import routers
from .views import PessoasViewSet, hello_world


router = routers.DefaultRouter()
router.register(r'pessoas', PessoasViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('hello/', hello_world, name='hello'),
    path('api-auth/', include(
        'rest_framework.urls', namespace='rest_framework'))
]
