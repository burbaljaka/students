from django.urls import path
from .views import MarkViewset, StudentViewset
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('students', StudentViewset)
router.register('marks', MarkViewset)

urlpatterns = router.urls