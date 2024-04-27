from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


from mainapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('users.urls')),

    path('', views.home, name='home'),
    path('my_report/', views.reports_user, name='user_report'),

    path('all-reports/', views.all_reports, {'endpoint': 'all_reports'}, name='all_reports'),
    path('new-report/', views.all_reports, {'endpoint': 'new_report'}, name='new_report'),
    path('verify-reports/', views.all_reports, {'endpoint': 'verify_reports'}, name='verify_reports'),

    path('verify-report/<int:operation_id>/', views.verify_report, name='verify_report'),
    path('rejected-report/<int:operation_id>/', views.rejected_report, name='rejected_report'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)