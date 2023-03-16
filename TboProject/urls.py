from rest_framework import routers

from TboProject.views import ObjectAPIView

router = routers.SimpleRouter()
router.register(r'api/objects', ObjectAPIView)

urlpatterns = router.urls
