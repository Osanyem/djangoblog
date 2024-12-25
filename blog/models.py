from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    """
    A Django model representing a blog post.

    Attributes:
        author (ForeignKey): A foreign key to the user who authored the post.
        title (CharField): The title of the post, with a maximum length of 200 characters.
        text (TextField): The main content of the post.
        created_date (DateTimeField): The date and time when the post was created, defaults to the current time.
        published_date (DateTimeField): The date and time when the post was published, can be blank or null.

    Methods:
        publish(): Sets the published_date to the current time and saves the post.
        __str__(): Returns the title of the post as its string representation.
    """

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
