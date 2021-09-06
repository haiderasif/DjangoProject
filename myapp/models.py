from django.db import models

# Create your models here.
class Booking(models.Model):
    username=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    noofpeople=models.IntegerField(max_length=100)
    date=models.DateField(max_length=100)
    time=models.TimeField()
    info=models.CharField(max_length=100)

    
class BoardOfDirector(models.Model):
    bod_id = models.IntegerField(db_column='BOD_ID', primary_key=True)  # Field name made lowercase.
    bod_name = models.CharField(db_column='BOD_name', max_length=20)  # Field name made lowercase.
    bod_tagline = models.CharField(db_column='BOD_TAGLINE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    bod_quote = models.CharField(db_column='BOD_QUOTE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bod_pic = models.CharField(db_column='BOD_PIC', max_length=567, blank=True, null=True)  # Field name made lowercase.
    bod_qualification = models.CharField(db_column='BOD_QUALIFICATION', max_length=20, blank=True, null=True)  # Field name made lowercase.
    bod_social = models.CharField(db_column='BOD_Social', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Board_of_director'


class Department(models.Model):
    dept_id = models.IntegerField(primary_key=True)
    dept_name = models.CharField(max_length=20, blank=True, null=True)
    no_of_members = models.IntegerField(blank=True, null=True)
    project_assigned = models.IntegerField(db_column='Project_assigned', blank=True, null=True)  # Field name made lowercase.
    dept_location = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Department'


class Employee(models.Model):
    emp_id = models.IntegerField(db_column='Emp_ID', primary_key=True)  # Field name made lowercase.
    emp_name = models.CharField(db_column='Emp_Name', max_length=20)  # Field name made lowercase.
    social_media = models.CharField(db_column='Social_Media', max_length=30, blank=True, null=True)  # Field name made lowercase.
    emp_pic = models.CharField(db_column='Emp_Pic', max_length=20)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=220, blank=True, null=True)  # Field name made lowercase.
    designation = models.CharField(db_column='Designation', max_length=40, blank=True, null=True)  # Field name made lowercase.
    seniority = models.CharField(db_column='Seniority', max_length=20, blank=True, null=True)  # Field name made lowercase.
    joining_date = models.DateField(db_column='Joining_Date', blank=True, null=True)  # Field name made lowercase.
    pay_scale = models.IntegerField(db_column='Pay_Scale', blank=True, null=True)  # Field name made lowercase.
    salary = models.IntegerField(db_column='Salary', blank=True, null=True)  # Field name made lowercase.
    allowed_holidays = models.IntegerField(db_column='Allowed_holidays', blank=True, null=True)  # Field name made lowercase.
    availed_holidays = models.IntegerField(db_column='Availed_holidays', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EMPLOYEE'

