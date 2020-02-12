from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from pessoa import urls as pessoa_urls
from django.contrib.auth import views as auth_views
from pessoa.views import home

urlpatterns = [
    path('', home),
    path('pessoa/', include(pessoa_urls)),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
