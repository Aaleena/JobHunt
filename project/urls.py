from django.urls import path
from . import views

urlpatterns=[path('',views.JobListView.as_view(),name='home'),
	path('post/<int:pk>/',views.JobDetailView.as_view(),name='job_detail'),
]
