from django.contrib import auth
from django.db import models


class Publisher(models.Model):
    """A company that publishes books."""
    name = models.CharField(help_text="The name of the Publisher.", max_length=255)
    website = models.URLField(help_text="The Publisher's website.")
    email = models.EmailField(help_text="The Publisher's email address.")

    def __str__(self):
        return self.name


class Contributor(models.Model):
    """A contributor to a Book, e.g. author, editor, co-author."""
    first_names = models.CharField(help_text="The contributor's first name or names.", max_length=255)
    last_names = models.TextField(help_text="The contributor's last name or names.")
    email = models.EmailField(help_text="The contact email for the contributor.")
    def __str__(self):
        return "%s %s" % (self.first_names, self.last_names)

class Book(models.Model):
    """A published book."""
    title = models.CharField(help_text="The title of the book.", max_length=255)
    publication_date = models.DateField(verbose_name="Date the book was published.")
    isbn = models.CharField(verbose_name="ISBN number of the book.", max_length=20)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    contributors = models.ManyToManyField(Contributor, through="BookContributor")

    def __str__(self):
        return self.title


class BookContributor(models.Model):
    class ContributionRole(models.TextChoices):
        AUTHOR = "AUTHOR", "Author"
        CO_AUTHOR = "CO_AUTHOR", "Co-Author"
        EDITOR = "EDITOR", "Editor"

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    role = models.TextField(verbose_name="The role this contributor had in the book.", choices=ContributionRole.choices)


class Review(models.Model):
    content = models.TextField(help_text="The Review text.")
    rating = models.IntegerField(help_text="The the reviewer has given.")
    date_created = models.DateTimeField(auto_now_add=True, help_text="The date and time the review was created.")
    date_edited = models.DateTimeField(null=True,
                                       help_text="The date and time the review was last edited (null if it was not "
                                                 "edited)."
                                       )
    creator = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, help_text="The Book that this review is for.")


