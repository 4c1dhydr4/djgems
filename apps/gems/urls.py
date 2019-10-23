from django.contrib.auth.decorators import login_required
from django.urls import path, include
from rest_framework import routers
from apps.gems.views import index, login, GemsView, GemProfileView

router = routers.DefaultRouter()
router.register('gems', GemsView)
router.register('users', GemProfileView)

app_name="gems"

urlpatterns = [
	path('', login_required(index), name="index"),
	path('api/', include(router.urls)),
	# path('login/', login, name="login"),
]