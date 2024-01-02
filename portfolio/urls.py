from django.urls import path
from . import views

urlpatterns = [
    path('',views.Index,name='home'),
    path('my-skills/',views.MySkills,name='skills'),
    path('my-projects/',views.MyProjects,name='projects'),
    path('my-projects/<int:id>/',views.ProjectDetails,name='detail'),
    path('my-resume/',views.Resume,name='resume'),
    path('download-resume/<int:file_id>/', views.Download_resume, name='download'),
    path('contact-us/',views.Contact,name='contact'),

]