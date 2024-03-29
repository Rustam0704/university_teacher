from django.urls import path

from courses.views import home_page, teacher_detail, speciality_detail, speciality_create, teacher_create

app_name = "courses"
urlpatterns = [
    path('', home_page, name='home-page'),
    path('teacher/create', teacher_create, name='teacher-create'),
    path('specility/create', speciality_create, name='speciality-create'),
    path('teacher/<id>', teacher_detail, name='teacher-detail'),
    path('specility/<id>', speciality_detail, name='speciality-detail'),
]
