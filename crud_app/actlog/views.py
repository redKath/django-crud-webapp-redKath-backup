from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, View
from .models import ActivityLogTable, ActivityLog
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
import django_tables2 as tables

# importing get_template from loader
from django.template.loader import get_template

# import render_to_pdf from util.py
from .utils import render_to_pdf

# Create your views here.
@login_required
def home(request):
	context = {
			 'activities': ActivityLog.objects.all()
	}

	return render(request, 'actlog/home.html', context)


@login_required
def about(request):
	return render(request, 'actlog/about.html', {'title': 'About'})


class ActivityLogListView(LoginRequiredMixin, ListView):

	context_object_name = 'activities'
	table_class = ActivityLogTable
	fields = ['activity', 'rhr', 'ahr', 'day', 'highday']

	queryset = ActivityLog.objects.all()
	template_name = "actlog/act-page.html"


class ActivityLogCreateView(LoginRequiredMixin, CreateView):  # CREATE of  activities
	model = ActivityLog
	fields = ['activity', 'rhr', 'ahr', 'day', 'highday']


class ActivityLogDetailView(LoginRequiredMixin, DetailView):  # view of all activities
	model = ActivityLog


class ActivityLogUpdateView(LoginRequiredMixin, UpdateView):  # CREATE of  activities
	model = ActivityLog
	fields = ['activity', 'rhr', 'ahr', 'day', 'highday']


class ActivityLogDeleteView(LoginRequiredMixin, DeleteView):  # view of all activities
	model = ActivityLog
	success_url = '/actlog/'


# Creating our view, it is a class based view
class GeneratePdf(View):
	def get(self, request, *args, **kwargs):
		data = {
			 'activities': ActivityLog.objects.all()
	}
		# getting the template
		pdf = render_to_pdf('actlog/act-page.html', data)
		# rendering the template
		return HttpResponse(pdf, content_type='application/pdf')
