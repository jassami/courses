from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_course', views.add_course),
    path('courses/destroy/<int:course_id>', views.remove),
    path('delete/<int:course_id>', views.delete),
    path('comments/<int:course_id>', views.comments),
]