from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from apps.gems.views import login

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('login/', login, name='login'),
    path('', include('apps.gems.urls', namespace='gems')),
	path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html')),
]
