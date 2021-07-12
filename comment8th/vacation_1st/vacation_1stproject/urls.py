from django.contrib import admin
from django.urls import path, include
import postcrud.views
import commentcrud.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', postcrud.views.list),
    path('postcrud/', include('postcrud.urls')),
    path('commentcrud/', include('commentcrud.urls')),
]
