from django.db import models


class NewsLetter(models.Model):
    """
    Model representing a newsletter subscriber.

    Attributes:
        email (EmailField): Email address of the subscriber.
        created_at (DateTimeField): Date and time when the subscriber was added.
    """

    email = models.EmailField(max_length=60)  # Unique email address of the subscriber
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the subscriber was added

    def __str__(self):
        return self.email  # String representation of the newsletter subscriber (email address)


class NewsLetterContent(models.Model):
    """
    Model representing the content of a newsletter.

    Attributes:
        title (CharField): Title of the newsletter content.
        content (TextField): Main content of the newsletter.
        created_at (DateTimeField): Date and time when the content was created.
    """

    title = models.CharField(max_length=100)  # Title of the newsletter content
    content = models.TextField()  # Main content of the newsletter
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the content was created

    def __str__(self) -> str:
        return self.title  # String representation of the newsletter content (title)
