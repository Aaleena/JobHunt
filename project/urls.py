from django.urls import path
from . import views

urlpatterns=[path('',views.JobListView.as_view(),name='home'),
	path('post/<int:pk>/',views.JobDetailView.as_view(),name='job_detail'),
	path('category/it/',views.IT.as_view(),name='it'),
	path('category/it/<int:pk>/',views.ITDetailView.as_view(),name='job_detail_it'),
	path('category/teaching/',views.Teaching.as_view(),name='teaching'),
	path('category/teaching/<int:pk>/',views.TeachingDetailView.as_view(),name='job_detail_teaching'),
	path('category/banking/',views.Banking.as_view(),name='banking'),
	path('category/banking/<int:pk>/',views.BankingDetailView.as_view(),name='job_detail_banking'),
	path('category/marketing/',views.Marketing.as_view(),name='marketing'),
	path('category/marketing/<int:pk>/',views.MarketingDetailView.as_view(),name='job_detail_marketing'),
]
