# Generated by Django 2.2.3 on 2020-01-02 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actlog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitylog',
            name='sched',
            field=models.CharField(choices=[('Monday 7:30 A.M. - 9:30 A.M.', 'MON 730H-0930H'), ('Monday 9:30 A.M. - 11:30 A.M.', 'MON 0930H-1130H'), ('Monday 11:30 A.M. - 1:30 P.M.', 'MON 1130H-0130H'), ('Monday 1:30 P.M. - 3:30 P.M.', 'MON 0130H-0330H'), ('Monday 3:30 P.M. - 5:30 P.M.', 'MON 0330H-0530H'), ('Monday 5:30 P.M. - 7:30 P.M.', 'MON 0530H-0730H'), ('Tuesday 7:30 A.M. - 9:30 A.M.', 'TUE 0730H-0930H'), ('Tuesday 9:30 A.M. - 11:30 A.M.', 'TUE 0930H-1130H'), ('Tuesday11:30 A.M. - 1:30 P.M.', 'TUE 1130H-0130H'), ('Tuesday 1:30 P.M. - 3:30 P.M.', 'TUE 0130H-0330H'), ('Tuesday 3:30 P.M. - 5:30 P.M.', 'TUE 0330H-0530H'), ('Tuesday 5:30 P.M. - 7:30 P.M.', 'TUE 0530H-0730H'), ('Wednesday 7:30 A.M. - 9:30 A.M.', 'WED 0730H-0930H'), ('Wednesday 9:30 A.M. - 11:30 A.M.', 'WED 0930H-1130H'), ('Wednesday 11:30 A.M. - 1:30 P.M.', 'WED 1130H-0130H'), ('Wednesday 1:30 P.M. - 3:30 P.M.', 'WED 0130H-0330H'), ('Wednesday 3:30 P.M. - 5:30 P.M.', 'WED 0330H-0530H'), ('Wednesday 5:30 P.M. - 7:30 P.M.', 'WED 0530H-0730H'), ('Thursday 7:30 A.M. - 9:30 A.M.', 'THU 0730H-0930H'), ('Thursday 9:30 A.M. - 11:30 A.M.', 'THU 0930H-1130H'), ('Thursday 11:30 A.M. - 1:30 P.M.', 'THU 1130H-0130H'), ('Thursday 1:30 P.M. - 3:30 P.M.', 'THU 0130H-0330H'), ('Thursday 3:30 P.M. - 5:30 P.M.', 'THU 0330H-0530H'), ('Thursday 5:30 P.M. - 7:30 P.M.', 'THU 0530H-0730H'), ('Friday 7:30 A.M. - 9:30 A.M.', 'FRI 0730H-0930H'), ('Friday 9:30 A.M. - 11:30 A.M.', 'FRI 0930H-1130H'), ('Friday 11:30 A.M. - 1:30 P.M.', 'FRI 1130H-0130H'), ('Friday 1:30 P.M. - 3:30 P.M.', 'FRI 0130H-0330H'), ('Friday 3:30 P.M. - 5:30 P.M.', 'FRI 0330H-0530H'), ('Friday 5:30 P.M. - 7:30 P.M.', 'FRI 0530H-0730H')], default='Monday 7:30 A.M. - 9:30 A.M.', max_length=30),
        ),
    ]
