from django.urls import path
from . import views

urlpatterns = [
    path('<username>/', views.get_list_by_user),
    path('<username>/<int:articleId>', views.get_user_article), 
]