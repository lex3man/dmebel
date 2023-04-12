from django.urls import path, include

urlpatterns = [
    path('resources/', include('apps.res.urls')),
]
