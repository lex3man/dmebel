from django.urls import path, include

urlpatterns = [
    path('resources/', include('apps.res.urls')),
    # path('crm/', include('apps.crm.urls')),
    # path('tasks/', include('apps.tasks.urls')),
    # path('utils/', include('apps.utils.urls')),
]
