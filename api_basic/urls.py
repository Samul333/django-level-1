
from django.urls import path
from . views import article_list,student_list,studentDetails,studentCreate,studentUpdate
urlpatterns = [
    path('article/', article_list),
    path('students/', student_list),
    path('student-create/',studentCreate),
    path('studentall/<int:pk>/', studentDetails),
    path('studentupdate/<int:pk>/', studentUpdate)

]
