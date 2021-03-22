from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from gateau.views import new_gateau, voir_gateau, iscription, home, album, album_test, album_mixt
from gateau.api import gateau_API, gateau_detail_api, GateauListApi, GateauDetail, GateauAdd
from rest_framework import routers
from gateau import api

router = routers.DefaultRouter()
router.register('gateau', api.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('form/', new_gateau),
    path('album_mixt/', album_mixt),
    path('album_test/', album_test),
    path('iscription/', iscription),
    path('album/', album),
    path('home/', home),
    path('image/', voir_gateau),
    path('api-auth/', include('rest_framework.urls')),
    #api fonction classique
    path('api/gateaux/', gateau_API, name = 'gatAPI'),
    path('api/gateaux/<int:id>', gateau_detail_api, name = 'gateau_detail_api'),

    # api class générique GEt
    path('api/v2/gateaux/', GateauListApi.as_view(), name = 'gatAPI'),
    # api class générique RUD
    path('api/v2/gateaux/<int:id>', GateauDetail.as_view(), name = 'gateau_detail_api'),
    # api class générique Create
    path('api/v2/gateaux/add', GateauAdd.as_view(), name = 'gatAPI'),

    # api viewsets 


]


if settings.DEBUG:
    if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
