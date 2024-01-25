from django.urls import path
from projects_app import views
from .views import home, add_project, delete_project

urlpatterns = [
    path('',views.home,name='home'),
    path('createproject/',views.add_project,name='addproject'),
    path('delete/<int:project_id>/', delete_project, name='delete_project'),
]
