from django.db import models

class Author(models.Model):
    author_name = models.CharField(max_length=100)
    author_title = models.TextField(default="Untitled")
    author_type = models.CharField(max_length=100)
    author_department = models.CharField(max_length=100)
    employee_number = models.CharField(max_length=100)

    def __str__(self):
        return self.author_name

class Study(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='studies', null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    abstract = models.TextField()
    keywords = models.CharField(max_length=200)
    status = models.CharField(max_length=100)
    date_started = models.DateField()
    researchers = models.TextField()
    file = models.FileField(upload_to='studies/', null=True, blank=True)

    def __str__(self):
        return self.title

