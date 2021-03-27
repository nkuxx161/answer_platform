from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('student', views.StudentView)
router.register('teacher', views.TeacherView)
router.register('teachingAdmin', views.TeachingAdminView)
router.register('lesson', views.LessonView)
router.register('teacherClass', views.TeacherClassView)
router.register('studentClass', views.StudentClassView)
router.register('chatting', views.ChattingView)
router.register('waitLine', views.WaitLineView)
urlpatterns = [
    path('', include(router.urls))
]
