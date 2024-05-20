from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, user_name, user_email, ID, user_mood, user_energy, user_tempo, password=None):
        if not user_name:
            raise ValueError('사용자는 무조건 이름이 있어야 합니다.')
        
        if not user_email:
            raise ValueError('사용자는 무조건 이메일이 있어야 합니다.')
        
        if not ID:
            raise ValueError('사용자는 무조건 ID가 있어야 합니다.')
        
        
        user = self.model(
            email = self.normalize_email(user_email),
            user_name = user_name,
            ID = ID,
            user_mood = user_mood,
            user_energy = user_energy,
            user_tempo = user_tempo,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, )




class User(AbstractBaseUser):
    pass




# 지민이 언니 실험용
class UploadMAXMIN(models.Model):
    max_file = models.FileField(upload_to='userVoice/')
    min_file = models.FileField(upload_to='userVoice/')

class MaxminNote(models.Model):
    max_note =models.CharField(max_length=5)
    min_note =models.CharField(max_length=5)

