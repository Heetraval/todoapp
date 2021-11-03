from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name="home"),
    path('add', views.add, name="add"),
    path('del_todo/<int:todo_id>', views.deltodo, name="deltodo")
]