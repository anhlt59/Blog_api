from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings

# Post model
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

# Create your models here...
class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """ Creates and saves a new user."""

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """ Creates and saves a new super user."""

        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin, TimeStampMixin):
    """ Custom user model that support using email instead of username."""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name',]

    def __str__(self):
        """Return string representation of user"""
        return self.email


class Tag(models.Model):
    """Tag to be used for a post"""
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        User, #settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Post(TimeStampMixin):
    """ Post object."""
    author = models.ForeignKey(
        User,
        # settings.AUTH_USER_MODEL,
        on_delete= models.CASCADE,
        related_name='blog_posts'
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    # tags = models.ManyToManyField('Tag')
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    # image = models.ImageField(null=True, upload_to=post_image_file_path)

    REQUIRED_FIELDS = ['slug', 'title']

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
