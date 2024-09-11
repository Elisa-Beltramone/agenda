from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<int:year>/<str:month>', views.home, name="home"),
    path('planner', views.planner, name="planner"),
    path('add_event', views.add_event, name="add_event"),
    path('show_event/<event_id>', views.show_event, name="show_event"),
    path('search/', views.searched, name="search"),
    path('update_event/<event_id>', views.update_event, name="update_event"),
    path('delete_event/<event_id>', views.delete_event, name="delete_event"),
    path('my_agenda/', views.my_agenda, name="agenda"),
    path('event_text', views.event_text, name="event_text")
]