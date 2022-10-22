from django.db import models
import secrets
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
curId = ""
def generate_id():
    length = 32
    id = secrets.token_hex(32)
    """ #TODO - check if id already exists in database
    while True:
        id = secrets.token_hex(32)
        if User.objects.filter(id=code).count() == 0:
            break
    """
    curId = str(id)
    return id

class UserManager(BaseUserManager):

    def create_user(self, username, github, profileImage="https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png", password=None, **kwargs):
        """Create and return a `User` with an email, phone number, username and password."""
        if username is None:
            raise TypeError('Users must have a username.')
        if github is None:
            raise TypeError('Users must have an github.')

        user = self.model(username=username, displayName=username, github=github, profileImage=profileImage)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, github, password):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')
        if github is None:
            raise TypeError('Superusers must have github.')
        if username is None:
            raise TypeError('Superusers must have an username.')

        user = self.create_user(username, github, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    type = models.CharField(max_length=32, default="author")
    id = models.CharField(max_length=128, primary_key=True, default=generate_id)
    url = models.CharField(max_length=255, default = "")
    host = models.CharField(max_length=255, default= "http://127.0.0.1:8000/")
    username = models.CharField(db_index=True, max_length=255, unique=True)
    displayName = models.CharField(max_length=255, default="")
    #email = models.EmailField(db_index=True, unique=True,  null=True, blank=True)
    github = models.URLField(db_index=True, unique=True,  null=True, blank=True)
    profileImage = models.URLField(max_length=500, default="https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'github'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return f"{self.github}"

    def save(self, *args, **kwargs):
        self.url = "http://127.0.0.1:8000/authors/" + self.id
        return super(User, self).save(*args, **kwargs)