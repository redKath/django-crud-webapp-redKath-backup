from django.urls import path
from . import views
from .views import ActivityLogListView, ActivityLogCreateView, ActivityLogDetailView, ActivityLogUpdateView, ActivityLogDeleteView
from .views import GeneratePdf

urlpatterns = [
	path('', views.home, name = 'actlog-home'),
	path('about/', views.about, name = 'actlog-about'),
	path('actlog/', ActivityLogListView.as_view(), name = 'actlog-view'),
	path('actlog/<int:pk>/', ActivityLogDetailView.as_view(), name = 'actlog-detail'),
	path('actlog/<int:pk>/update/', ActivityLogUpdateView.as_view(), name = 'actlog-update'),
	path('actlog/<int:pk>/delete/', ActivityLogDeleteView.as_view(), name = 'actlog-delete'),
	path('actlog/new/', ActivityLogCreateView.as_view(), name = 'actlog-create'),
	path('actlog/new/', ActivityLogCreateView.as_view(), name = 'actlog-create'),
	path('actlog/pdf/', GeneratePdf.as_view(), name = 'actlog-pdf')



]