# Create your models here.

from django.db import models

# Model for individual expenses
class IndividualExpense(models.Model):
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return f"Individual: {self.name}"

# Model for group expenses
# class GroupExpense(models.Model):
#     name = models.CharField(max_length=200)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     date = models.DateField()
#     category = models.CharField(max_length=100)
#     is_group = models.BooleanField(default=True)
    
#     # Fields for members (assuming there are exactly 5 members)
#     member1 = models.CharField(max_length=100, blank=True, null=True)
#     member2 = models.CharField(max_length=100, blank=True, null=True)
#     member3 = models.CharField(max_length=100, blank=True, null=True)
#     member4 = models.CharField(max_length=100, blank=True, null=True)
#     member5 = models.CharField(max_length=100, blank=True, null=True)

#     def __str__(self):
#         return self.name


class Member(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class GroupExpense(models.Model):
    name = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    category = models.CharField(max_length=100)
    is_group = models.BooleanField(default=True)

    # Many-to-Many Relationship with Members
    members = models.ManyToManyField(Member, related_name="group_expenses")

    def __str__(self):
        return self.name

