from django.urls import path,include
from .views import *


from users.urls import *

urlpatterns =[
    path('get-all-students',GetStudents.as_view(),),

]