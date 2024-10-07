from django import forms
from .models import User, UserProfile
from .validators import allow_only_images_validator


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter First Name', 'required': 'required'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter First Name', 'required': 'required'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter First Name', 'required': 'required'}))
    # middle_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Middle Name', 'required': 'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Last Name', 'required': 'required'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Username ', 'required': 'required'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Email', 'required': 'required'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Phone Number', 'required': 'required'}))
    # gender = forms.CharField(widget=forms.TextInput(attrs={}))
    # staff_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Staff ID', 'required': 'required'}))
    # role = forms.Select()

    class Meta:
        model = User
        fields = ['profile_picture','first_name', 'last_name', 'username', 'email', 'role', 'password']

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                "Password does not match!"
            )
        


class UserProfileForm(forms.ModelForm):
   

    
    
    class Meta:
        model = UserProfile
        fields = []

class UserProfilePictureForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['profile_picture']




from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model

User = get_user_model()

class UserEditForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'phone_number', 'profile_picture', 'role', 'is_active', 'is_admin', 'is_staff', 'is_superadmin')

    def clean_password(self):
        return self.initial["password"]

class PasswordChangeForm(forms.ModelForm):
    old_password = forms.CharField(widget=forms.PasswordInput)
    new_password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('old_password', 'new_password', 'confirm_password')

    def clean(self):
        cleaned_data = super().clean()
        old_password = cleaned_data.get("old_password")
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")

        if not self.instance.check_password(old_password):
            self.add_error('old_password', 'Old password is incorrect')

        if new_password != confirm_password:
            self.add_error('confirm_password', 'New password and confirm password do not match')

        return cleaned_data
