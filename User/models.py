from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager



class UserManager(BaseUserManager):
    def create_user(self,email,password = None,password2=None,**extra_fields):
        if not email:
            raise ValueError('email must be provided')

        user = self.model(
            
            email = email,
            **extra_fields
            )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email,password, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        return self.create_user(email,password,**extra_fields)


#user model
class User(AbstractUser):
    email = models.EmailField(max_length=30,unique=True)
    created_time_stamp = models.DateTimeField(auto_now_add=True)
    update_by_time_stamp = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True, blank=True)
    is_admin = models.BooleanField(default=False, blank=True)

    objects = UserManager()
    # USERNAME_FIELD = "email"
    # REQUIRED_FIELD = []
    




