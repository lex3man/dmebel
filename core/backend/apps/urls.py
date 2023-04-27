from django.urls import path, include
from .api import GetData

urlpatterns = [
    # path('resources/', include('apps.res.urls')),
    # path('crm/', include('apps.crm.urls')),
    # path('tasks/', include('apps.tasks.urls')),
    path('utils/', include('apps.utils.urls')),
    path('tasks/', GetData.as_view(), name='api_tasks')
]
