from django.contrib import admin
from django.urls import path, include
from users.views import Login, Logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario/', include('users.api.urls')),
    path('', Login.as_view(), name = 'login'),
    path('logout', Logout.as_view(), name = 'logout'),
    path('tareas/', include('tasks.api.urls')),
]
