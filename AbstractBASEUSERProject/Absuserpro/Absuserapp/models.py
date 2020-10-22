

from django.db import models

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):


    def create_user(self, email, username, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        if not username:
            raise ValueError("User must have an Username")
        user = self.model(
            email=self.normalize_email(email),
            username = username,
            )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, email):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
            username = username,
            )
        user.is_admin =  True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user 

       
class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=50, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin    

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


