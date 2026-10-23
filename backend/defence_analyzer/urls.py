from django.urls import path, include
from ai_engine import views as ai_views

urlpatterns = [
    path('', ai_views.index_view, name='root_index'),
    path('favicon.ico', ai_views.favicon, name='favicon'),
    path('api/', include('ai_engine.urls')),
]
