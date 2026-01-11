from django.db import models
from django.utils import timezone

# Admin model
class AdminLogin(models.Model):
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    username = models.CharField(max_length=150, unique=True, default="admin_user", null=True, blank=True)
    password = models.CharField(max_length=128, default="default_password123", null=True, blank=True)
    admin_name = models.CharField(max_length=100, default="Default Admin", null=True, blank=True)
    mobile = models.CharField(max_length=15, default="0000000000", null=True, blank=True)
    email_id = models.EmailField(max_length=255, unique=True, default="admin@example.com", null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Active', null=True, blank=True)


    def __str__(self):
        return f"{self.admin_name} ({self.username})"

# Department model
class DepartmentDetails(models.Model):
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    dept_id = models.AutoField(primary_key=True)
    department = models.CharField(max_length=100, null=True, blank=True)
    department_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Active', null=True, blank=True)

    def __str__(self):
        return f"{self.department} ({self.department_status})"

# Complaint type
class ComplaintType(models.Model):
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    complain_id = models.AutoField(primary_key=True)
    complain = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Active', null=True, blank=True)

    def __str__(self):
        return f"{self.complain_id} | {self.complain} | {self.status}"

# Complaint description
class ComplaintDescription(models.Model):
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    complain_desc_id = models.AutoField(primary_key=True)
    complain_type = models.ForeignKey(ComplaintType, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Active', null=True, blank=True)

    def __str__(self):
        return f"{self.complain_desc_id} | {self.complain_type} | {self.description} | {self.status}"

# IT Team model
class ITTeam(models.Model):
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    it_team_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True, null=True, blank=True)
    password = models.CharField(max_length=128, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    mobile = models.CharField(max_length=15, null=True, blank=True)
    email_id = models.EmailField(max_length=255, null=True, blank=True)
    create_dt = models.DateTimeField(default=timezone.now, null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Active', null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.username}) - {self.status}"

# User details
class UserDetails(models.Model):
    user_id = models.AutoField(primary_key=True)
    dept = models.ForeignKey(DepartmentDetails, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=150, null=True, blank=True)
    user_ip = models.GenericIPAddressField(null=True, blank=True)
    system_name = models.CharField(max_length=100, null=True, blank=True)
    mobile = models.CharField(max_length=15, null=True, blank=True)
    email_id = models.EmailField(max_length=255, null=True, blank=True)
    # user_create_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.username} ({self.email_id})"

# User complaint
class UserComplain(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
        ('Closed', 'Closed'),
    )
    user_complain_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE, null=True, blank=True)
    department = models.ForeignKey(DepartmentDetails, on_delete=models.CASCADE, null=True, blank=True)
    complain_type = models.ForeignKey(ComplaintType, on_delete=models.CASCADE, null=True, blank=True)
    complain_desc = models.ForeignKey(ComplaintDescription, on_delete=models.CASCADE, null=True, blank=True)
    it_team = models.ForeignKey(ITTeam, on_delete=models.SET_NULL, null=True, blank=True)
    email_id = models.EmailField(max_length=255, null=True, blank=True)
    complain_dt = models.DateField(null=True, blank=True)
    complain_time = models.TimeField(null=True, blank=True)
    resolve_dt = models.DateField(null=True, blank=True)
    resolve_time = models.CharField(max_length=50, null=True, blank=True)
    complain_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending', null=True, blank=True)