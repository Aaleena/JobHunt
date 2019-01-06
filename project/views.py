from django.views.generic import ListView,DetailView

from .models import Post

class JobListView(ListView):
	model=Post
	template_name='home.html'

class JobDetailView(DetailView):
	model=Post
	template_name='job_detail.html'

class MarketingDetailView(DetailView):
	model=Post
	template_name='job_detail_marketing.html'
class TeachingDetailView(DetailView):
	model=Post
	template_name='job_detail_teaching.html'
class BankingDetailView(DetailView):
	model=Post
	template_name='job_detail_banking.html'
class ITDetailView(DetailView):
	model=Post
	template_name='job_detail_it.html'

class IT(ListView):
	model=Post
	template_name='it.html'

class Teaching(ListView):
	model=Post
	template_name='teaching.html'

class Banking(ListView):
	model=Post
	template_name='banking.html'

class Marketing(ListView):
	model=Post
	template_name='marketing.html'

