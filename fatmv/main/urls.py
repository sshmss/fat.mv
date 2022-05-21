from main.views import UserViewSet, TrainerViewSet, MemberViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'trainers', TrainerViewSet, basename='trainer')
router.register(r'members', MemberViewSet, basename='member')
urlpatterns = router.urls