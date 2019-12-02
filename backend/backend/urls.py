from django.contrib import admin
from django.urls import path, include
from todos.views import Todo_Viewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'todos', Todo_Viewset)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]