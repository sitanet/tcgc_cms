from django.db import models
from datetime import date
from accounts.models import User
from follow_up_project import settings


class Pastorate(models.Model):
    # name = models.CharField(max_length=100)
    name = models.ForeignKey(User, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.name

    def __str__(self):
        return str(self.name)

# Create your models here.
class Team_Lead(models.Model):
   
    name = models.ForeignKey(User, on_delete=models.CASCADE)
   

    def __str__(self):
        return str(self.name)
    
   

class TeamMember(models.Model):
    # name1 = models.CharField(max_length=15, blank=True, null=True)
    team_lead = models.ForeignKey(Team_Lead, on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.name\
    def __str__(self):
        return str(self.name)

class Member(models.Model):
    
    MALE = 1
    FEMALE = 2
    SINGLE = 1
    MARRIED = 2
    TEENAGER = 3
    CHILDREN = 4
    PRIVATE = 1
    STATE = 2
    FEDERAL = 3
    ACTIVE = 1
    INACTIVE = 2

    
    
    GENDER = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
       
    )
    
    MARITAL = (
        (SINGLE, 'Single'),
        (MARRIED, 'Married'),
        (TEENAGER, 'Teenager'),
        (CHILDREN, 'Children'),
       
    )

    STATUS = (
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
       
    )

  

    image = models.ImageField(upload_to='images/')
    first_name = models.CharField(max_length=52)
    middle_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()

    email = models.EmailField(max_length=52)
    phone_no = models.CharField(max_length=15)
    gender = models.PositiveIntegerField(choices=GENDER)
    marital_status = models.PositiveIntegerField(choices=MARITAL)
    occupation = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    nationality = models.CharField(max_length=20)
    kcc_center = models.CharField(max_length=20,blank=True, null=True)
    place_of_work = models.CharField(max_length=50,blank=True, null=True)
    position = models.CharField(max_length=40,blank=True, null=True)
    house_position = models.CharField(max_length=50, default="non-house-member")
    
    wedding_ann = models.DateField(blank=True, null=True)
    join = models.DateField(blank=True, null=True)
    # reg_date = models.CharField(max_length=20, blank=True, null=True)
    about = models.CharField(max_length=20,blank=True, null=True)
    dept = models.CharField(max_length=20,blank=True, null=True)
    purpose = models.CharField(max_length=20,blank=True, null=True)
    # team_lead = models.CharField(max_length=20, blank=True, null=True)
    # team_member = models.CharField(max_length=20, blank=True, null=True)


    # team_lead = models.ForeignKey(Team_Lead, on_delete=models.SET_NULL, null=True, blank=True)
    # team_member = models.ForeignKey(TeamMember, on_delete=models.SET_NULL, null=True, blank=True)

    
    team_lead = models.CharField(max_length=20,blank=True, null=True)
    team_member = models.CharField(max_length=20,blank=True, null=True)
   
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.PositiveIntegerField(choices=STATUS, default='1', blank=True)
    kin_fullname = models.CharField(max_length=50, blank=True, null=True)
    kin_birth = models.DateField(null=True, blank=True)
    kin_gender = models.CharField(max_length=20, blank=True, null=True)
    kin_relationship = models.CharField(max_length=20, blank=True, null=True)
    kin_address = models.CharField(max_length=100, blank=True, null=True)
    kin_phone_no = models.CharField(max_length=20, blank=True, null=True)
    kin_email = models.CharField(max_length=50, blank=True, null=True)
    emergency_phone_no = models.CharField(max_length=20, blank=True, null=True)


    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
  
 

    def __str__(self):
        if self.middle_name:
            return f"{self.first_name} {self.middle_name} {self.last_name}"
        return f"{self.first_name} {self.last_name}"



    

class Comment(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='comments')
    first_name = models.CharField(max_length=40, blank=False, null=False )
    last_name = models.CharField(max_length=25, blank=True, null=True)
    phone_no = models.CharField(max_length=25, blank=True, null=True)
    team_sup = models.ForeignKey(User, on_delete=models.CASCADE)
    team_mem = models.CharField(max_length=50, blank=True, null=True)
    coor_comm = models.CharField(max_length=30, blank=True, null=True)
    date_created = models.DateField(default=date.today, blank=True, null=True)
    comment = models.TextField()
  
   


    def __str__(self):
        return self.first_name






from django.db import models
from .models import Member

class Family(models.Model):
    husband = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='husband')
    wife = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='wife')

    family_name = models.CharField(max_length=100)
    
    team_lead = models.CharField(max_length=20, blank=True, null=True)
    team_member = models.CharField(max_length=20, blank=True, null=True)
  
    address = models.CharField(max_length=255)
    
    def __str__(self):
        return self.full_name



class Child(models.Model):
    family = models.ForeignKey(Family, on_delete=models.CASCADE, related_name='children')
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    




class Student(models.Model):
    UNDERGRADUATE = 'UG'
    POSTGRADUATE = 'PG'
    PROGRAM_CHOICES = [
        (UNDERGRADUATE, 'Undergraduate'),
        (POSTGRADUATE, 'Postgraduate'),
    ]

    INTERNSHIP = 'Internship'
    PART_TIME_JOB = 'Part-time job'
    WORK_TYPE_CHOICES = [
        (INTERNSHIP, 'Internship'),
        (PART_TIME_JOB, 'Part-time job'),
    ]

    member = models.OneToOneField(Member, on_delete=models.CASCADE)
    parent_address = models.CharField(max_length=255)
    parent_phone_number = models.CharField(max_length=15)
    university_name = models.CharField(max_length=255)
    program_of_study = models.CharField(max_length=255)
    program = models.CharField(max_length=2, choices=PROGRAM_CHOICES)
    work_type = models.CharField(max_length=50, choices=WORK_TYPE_CHOICES)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    duration = models.CharField(max_length=50, blank=True, null=True)  # E.g., "June 2020 - August 2020"
    responsibilities = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.member.first_name} {self.member.last_name} - {self.university_name}"






class NYSC(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    parent_address = models.CharField(max_length=255)
    parent_phone_number = models.CharField(max_length=20)
    university_name = models.CharField(max_length=100)
    program_of_study = models.CharField(max_length=100)
    year_of_graduation = models.IntegerField()
    place_of_assignment = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.university_name} - {self.program_of_study}"




class Children(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    class_name = models.CharField(max_length=50)  # 'class' is a reserved keyword in Python, so use 'class_name' instead
    allergies = models.TextField(blank=True, null=True)
    medical_conditions = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    




from django.db import models
from django.utils.translation import gettext as _

class Business(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=255)
    is_registered = models.BooleanField(default=False, verbose_name=_("Is business registered"))
    brief_description = models.TextField(blank=True)
    years_of_experience = models.PositiveIntegerField(default=0, verbose_name=_("Years of business experience"))
    number_of_employees = models.PositiveIntegerField(default=1)
    BUSINESS_SECTORS = [
        ("Technology", "Technology"),
        ("Finance", "Finance"),
        ("Healthcare", "Healthcare"),
        ("Education", "Education"),
        ("Manufacturing", "Manufacturing"),
        ("Real Estate", "Real Estate"),
        ("Hospitality", "Hospitality"),
        ("Retail", "Retail"),
        ("Entertainment", "Entertainment"),
        # Add more sectors as needed
    ]
    business_sector = models.CharField(max_length=100, choices=BUSINESS_SECTORS)

    def __str__(self):
        return self.business_name


class Career(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    skills = models.TextField(blank=True, null=True)
    achievements_and_awards = models.TextField(blank=True, null=True)
    additional_information = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"


class CurrentEmployment(models.Model):
    career = models.ForeignKey(Career, related_name='current_employments', on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100, blank=True, null=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    duration = models.CharField(max_length=100, blank=True, null=True)
    responsibilities = models.TextField(blank=True, null=True)
    

class PreviousEmployment(models.Model):
    career = models.ForeignKey(Career, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100, blank=True, null=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    duration = models.CharField(max_length=100, blank=True, null=True)
    responsibilities = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"

class EducationalBackground(models.Model):
    career = models.ForeignKey(Career, on_delete=models.CASCADE)
    degree = models.CharField(max_length=150, blank=True, null=True)
    institution = models.CharField(max_length=100, blank=True, null=True)
    year_of_graduation = models.PositiveIntegerField(blank=True, null=True)
    gpa = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.degree} from {self.institution}"

class OtherQualification(models.Model):
    career = models.ForeignKey(Career, on_delete=models.CASCADE)
    certification = models.CharField(max_length=100, blank=True, null=True)
    institution = models.CharField(max_length=100, blank=True, null=True)
    year_of_graduation = models.PositiveIntegerField(blank=True, null=True)
    gpa = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.certification





from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Household(models.Model):
    household_name = models.CharField(max_length=255)
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='current_households')
    past_username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='past_households')
    members = models.ManyToManyField(Member, through='HouseholdMember')

    def __str__(self):
        return self.household_name




from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class MemberQuery(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    past_username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='past_queries')
    query_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    reply_text = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Query by {self.user.username} on {self.member.first_name} {self.member.last_name}"



class HouseholdMember(models.Model):
    household = models.ForeignKey(Household, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.member} - {self.position}"




from django.db import models

class Teenager(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='teenagers')
    current_school_name = models.CharField(max_length=255)
    current_class = models.CharField(max_length=100)
    last_class_position = models.CharField(max_length=50)
    favorite_subjects = models.TextField()
    career_goals = models.TextField()
    college_plans = models.TextField(blank=True, null=True)
    other_future_aspirations = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.member.first_name} {self.member.last_name} - {self.current_school_name}"




from django.conf import settings
from django.db import models
from tinymce.models import HTMLField

# class Message(models.Model):
#     sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_messages')
#     recipient_role = models.PositiveSmallIntegerField(choices=User.ROLE_CHOICE)
#     subject = models.CharField(max_length=255)
#     body = HTMLField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     parent_message = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)

#     def __str__(self):
#         return self.subject







from django.db import models
from django.conf import settings


class Message(models.Model):
    # ForeignKey to link to the Member model
    member = models.ForeignKey('Member', on_delete=models.CASCADE)

    # ForeignKey to link to the sender (User model)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_combined_messages')

    # Field to specify the role of the recipient
    recipient_role = models.CharField(max_length=10)

    # Subject of the message
    subject = models.CharField(max_length=255)

    # Body of the message
    body = models.TextField()  # You can also use RichTextField if you're using CKEditor

    # Text of the query (if applicable)
    query_text = models.TextField(null=True, blank=True)

    # Text for replies (if applicable)
    reply_text = models.TextField(null=True, blank=True)

    # Username from a past household
    past_username = models.CharField(max_length=255, null=True, blank=True)

    # Timestamp for when the message was created
    created_at = models.DateTimeField(auto_now_add=True)

    # Optional: For threaded messages or replies
    parent_message = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.subject} by {self.sender.username} on {self.member.first_name} {self.member.last_name}"







# follow_app/models.py

class Notification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username} regarding {self.message.subject}"
