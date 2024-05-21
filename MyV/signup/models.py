from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone

class UserManager(BaseUserManager):
    def create_user(self, user_name, user_email, ID, user_mood, user_energy, user_tempo, password=None):
        if not user_name:
            raise ValueError('사용자는 무조건 이름이 있어야 합니다.')
        
        if not user_email:
            raise ValueError('사용자는 무조건 이메일이 있어야 합니다.')
        
        if not ID:
            raise ValueError('사용자는 무조건 ID가 있어야 합니다.')
        
        user = self.model(
            email=self.normalize_email(user_email),
            user_name=user_name,
            ID=ID,
            user_mood=user_mood,
            user_energy=user_energy,
            user_tempo=user_tempo,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, user_name, user_email, ID, user_mood, user_energy, user_tempo, password=None):
        user = self.create_user(
            email=self.normalize_email(user_email),
            user_name=user_name,
            ID=ID,
            user_mood=user_mood,
            user_energy=user_energy,
            user_tempo=user_tempo,
            password=password
        )
        
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using(self._db))
        return user

class User(AbstractBaseUser):
    user_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255, unique=True)
    ID = models.CharField(max_length=50, unique=True)
    user_mood = models.DecimalField(max_digits=4, decimal_places=2)
    user_energy = models.DecimalField(max_digits=4, decimal_places=2)
    user_tempo = models.DecimalField(max_digits=4, decimal_places=2)
    
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(default=timezone.now) 
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'ID', 'user_mood', 'user_energy', 'user_tempo']
    
    objects = UserManager()

    class Meta:
        app_label = 'signup'
    
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

class UploadMAXMIN(models.Model):
    max_file = models.FileField(upload_to='userVoice/')
    min_file = models.FileField(upload_to='userVoice/')

class MaxminNote(models.Model):
    max_note = models.CharField(max_length=5)
    min_note = models.CharField(max_length=5)
