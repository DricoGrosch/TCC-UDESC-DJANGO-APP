from django.urls import path, include

urlpatterns = [
    path('v1/', include('backend.core.api.v1.urls')),
]
