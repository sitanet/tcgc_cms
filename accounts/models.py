from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.fields.related import ForeignKey, OneToOneField




# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, role, phone_number,  password=None):
        if not email:
            raise ValueError('User must have an email address')

        if not username:
            raise ValueError('User must have an username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            role=role,
            phone_number=phone_number,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, username, email, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            role=User.ADMIN,  # Provide a role value here
            phone_number='N/A',  # Provide a phone_number value here
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user





class User(AbstractBaseUser):
    ADMIN = 1
    TEAM_LEAD = 2
    TEAM_MEMBER = 3
    PASTORATE = 4
    FACILITATOR = 5
    STUDENT = 6
    CARRER = 7
    BUSINESS = 8
    SERVICE_TEAM = 9
    MANAGEMENT_INFORMATION_SYSTEM = 10
    HOUSEHOLD_HEAD = 11
    KBN_CAREER = 12
    KBN_BUSINESS = 13

    MALE = 1
    FEMALE = 2

    ROLE_CHOICE = (
        (ADMIN, 'Admin'),
        (TEAM_LEAD, 'Team Lead'),
        (TEAM_MEMBER, 'Team Member'),
        (PASTORATE, 'Pastorate'),
        (FACILITATOR, 'Facilitator'),
        (STUDENT, 'Student'),
        (CARRER, 'Career'),
        (BUSINESS, 'Business'),
        (SERVICE_TEAM, 'Service Team'),
        (MANAGEMENT_INFORMATION_SYSTEM, 'Management Information System'),
        (HOUSEHOLD_HEAD, 'Household Head'),
        (KBN_CAREER, 'Kbn Career'),
        (KBN_BUSINESS, 'Kbn Business'),
    )

    profile_picture = models.ImageField(upload_to='users/profile_pictures', default='images/avatar.jpg')
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=110, unique=True)
    phone_number = models.CharField(max_length=30, blank=True, default='N/A')
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICE, default=ADMIN, blank=True, null=True)

    # required fields
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def get_role(self):
        role_mapping = {
            1: 'Admin',
            2: 'Team Lead',
            3: 'Team Member',
            4: 'Pastorate',
            5: 'KBN Facilitator',
            6: 'KBN Student',
            7: 'KBN Career',
            8: 'KBN Business',
            9: 'Service Team',
            10: 'Management Information System',
            11: 'Household Head',
            12: 'KBN Career',
            13: 'KBN Business',
        }
        return role_mapping.get(self.role, 'Unknown Role')

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


class UserProfile(models.Model):
    user = OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    # profile_picture = models.ImageField(upload_to='users/profile_pictures', blank=True, null=True)
    
    
    address = models.CharField(max_length=250, blank=True, null=True)
    country = models.CharField(max_length=15, blank=True, null=True)
    state = models.CharField(max_length=15, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
   
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    # def full_address(self):
    #     return f'{self.address_line_1}, {self.address_line_2}'

    def __str__(self):
        return self.user.email

