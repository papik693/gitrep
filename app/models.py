from django.db import models


class ImportBooks(models.Model):
    q = models.CharField(max_length=120)
    intitle = models.CharField(max_length=120, blank=True)
    inauthor = models.CharField(max_length=120, blank=True)
    inpublisher = models.CharField(max_length=120, blank=True)
    subject = models.CharField(max_length=120, blank=True)
    isbn = models.CharField(max_length=120, blank=True)
    lccn = models.CharField(max_length=120, blank=True)
    oclc = models.CharField(max_length=120, blank=True)


class Books(models.Model):
    title = models.CharField(max_length=120)
    authors = models.CharField(max_length=120)
    publishedDate = models.CharField(max_length=120)
    industryIdentifiers = models.CharField(max_length=120)
    pageCount = models.CharField(max_length=120)
    imageLinks = models.CharField(max_length=120)
    language = models.CharField(max_length=120)

    def __str__(self):
        return self.title
