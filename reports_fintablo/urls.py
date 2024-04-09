from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


from mainapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('users.urls')),

    path('', views.home, name='home'),
    path('my_report/', views.reports_user, name='user_report')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)