from django.urls import path
from . import views

urlpatterns = [
    path('http-response/', views.get_http_response),
    path('render/', views.get_render),
    path('render/pass-context-data/', views.get_render_pass_context_data),
]