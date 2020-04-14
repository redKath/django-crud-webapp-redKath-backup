from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
import django_tables2 as tables
# Create your models here.
class ActivityLog(models.Model):
	M1 = 'Monday 7:30 A.M. - 9:30 A.M.'
	M2 = 'Monday 9:30 A.M. - 11:30 A.M.'
	M3 = 'Monday 11:30 A.M. - 1:30 P.M.'
	M4 = 'Monday 1:30 P.M. - 3:30 P.M.'
	M5 = 'Monday 3:30 P.M. - 5:30 P.M.'
	M6 = 'Monday 5:30 P.M. - 7:30 P.M.'
	
	T1 = 'Tuesday 7:30 A.M. - 9:30 A.M.'
	T2 = 'Tuesday 9:30 A.M. - 11:30 A.M.'
	T3 = 'Tuesday 11:30 A.M. - 1:30 P.M.'
	T4 = 'Tuesday 1:30 P.M. - 3:30 P.M.'
	T5 = 'Tuesday 3:30 P.M. - 5:30 P.M.'
	T6 = 'Tuesday 5:30 P.M. - 7:30 P.M.'
	
	W1 = 'Wednesday 7:30 A.M. - 9:30 A.M.'
	W2 = 'Wednesday 9:30 A.M. - 11:30 A.M.'
	W3 = 'Wednesday 11:30 A.M. - 1:30 P.M.'
	W4 = 'Wednesday 1:30 P.M. - 3:30 P.M.'
	W5 = 'Wednesday 3:30 P.M. - 5:30 P.M.'
	W6 = 'Wednesday 5:30 P.M. - 7:30 P.M.'
	
	TH1 = 'Thursday 7:30 A.M. - 9:30 A.M.'
	TH2 = 'Thursday 9:30 A.M. - 11:30 A.M.'
	TH3 = 'Thursday 11:30 A.M. - 1:30 P.M.'
	TH4 = 'Thursday 1:30 P.M. - 3:30 P.M.'
	TH5 = 'Thursday 3:30 P.M. - 5:30 P.M.'
	TH6 = 'Thursday 5:30 P.M. - 7:30 P.M.'
	
	F1 = 'Friday 7:30 A.M. - 9:30 A.M.'
	F2 = 'Friday 9:30 A.M. - 11:30 A.M.'
	F3 = 'Friday 11:30 A.M. - 1:30 P.M.'
	F4 = 'Friday 1:30 P.M. - 3:30 P.M.'
	F5 = 'Friday 3:30 P.M. - 5:30 P.M.'
	F6 = 'Friday 5:30 P.M. - 7:30 P.M.'


	SCHED_CHOICES = [
			(M1,'MON 730H-0930H' ), (M2 , 'MON 0930H-1130H') ,(M3, 'MON 1130H-0130H'), 
			(M4, 'MON 0130H-0330H'), (M5, 'MON 0330H-0530H'), (M6,'MON 0530H-0730H'), 
			(T1, 'TUE 0730H-0930H'), (T2, 'TUE 0930H-1130H'), (T3, 'TUE 1130H-0130H'), 
			(T4, 'TUE 0130H-0330H'), (T5, 'TUE 0330H-0530H'), (T6,'TUE 0530H-0730H'), 
			(W1, 'WED 0730H-0930H'), (W2, 'WED 0930H-1130H'), (W3, 'WED 1130H-0130H'), 
			(W4, 'WED 0130H-0330H'), (W5, 'WED 0330H-0530H'), (W6,'WED 0530H-0730H'), 
			(TH1, 'THU 0730H-0930H'), (TH2, 'THU 0930H-1130H'), (TH3, 'THU 1130H-0130H'), 
			(TH4, 'THU 0130H-0330H'), (TH5, 'THU 0330H-0530H'), (TH6,'THU 0530H-0730H'), 
			(F1, 'FRI 0730H-0930H'), (F2, 'FRI 0930H-1130H'), (F3, 'FRI 1130H-0130H'), 
			(F4, 'FRI 0130H-0330H'), (F5, 'FRI 0330H-0530H'), (F6,'FRI 0530H-0730H'), 
	]

	
	activity = models.CharField(max_length = 50)
	rhr = models.IntegerField(validators = [MinValueValidator(45),MaxValueValidator(85)])
	ahr = models.IntegerField(validators = [MinValueValidator(75),MaxValueValidator(200)])
	day = models.DateField()
	highday = models.CharField(max_length = 100)
	
	def compare(rhr):
		if ahr < rhr:
			raise ValidationError(
			_('%(ahr) is less than your RHR.'),
			params={'ahr': ahr},)
	
	def __str__(self):
		return self.activity
	

	def get_absolute_url(self):
		return reverse('actlog-detail', kwargs={'pk':self.pk})
		
		
		
		
class ActivityLogTable(tables.Table):
	class Meta:
		model = ActivityLog
	