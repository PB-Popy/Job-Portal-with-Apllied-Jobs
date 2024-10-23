from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from myProject.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',signupPage,name="signupPage"),
    path("signInPage/", signInPage, name="signInPage"),
    path("homePage/", homePage, name="homePage"),
    path("logoutPage/", logoutPage, name="logoutPage"),
    path("ProfilePage/", profilePage, name="profilePage"),

    path("addJobPage/", addJobPage, name="addJobPage"),
    path("createdJobPage/", createdJobPage, name="createdJobPage"),
    
    path("jobFeed/", jobFeed, name="jobFeed"),

    path("deleteJob/<str:job_id>", deleteJob, name="deleteJob"),
    path("editJob/<str:job_id>", editJob, name="editJob"),
    path("viewJOb/<str:job_id>", viewJOb, name="viewJOb"),

    path('apply_now/<str:apply_id>',apply_now,name='apply_now'),
    path('appliedJob',appliedJob,name='appliedJob'),
    


    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)