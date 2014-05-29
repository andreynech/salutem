from django.db import models
from django.core.urlresolvers import reverse


class Author(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32, db_index = True)
    title = models.CharField(max_length=16)
    email = models.EmailField(max_length=254, db_index = True)
    organization = models.CharField(max_length=128, db_index = True)

    # On Python 3: def __str__(self):
    def __unicode__(self):
        return self.last_name + ' ' + self.first_name + " ("+self.organization+")"

    def get_absolute_url(self):
        return reverse('publications:author_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ('last_name', 'first_name',)
        unique_together = ('first_name', 'last_name', 'email')


class Article(models.Model):
    authors = models.ManyToManyField(Author, through='ArticleAuthors')
    headline = models.CharField(max_length=128, db_index = True)
    submit_date = models.DateTimeField(db_index = True, auto_now_add = True)
    abstract = models.TextField()
    abstract_en = models.TextField()
    article_url = models.URLField()

    # On Python 3: def __str__(self):
    def __unicode__(self):
        return self.headline

    def get_absolute_url(self):
        return reverse('publications:article_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ('headline',)


class ArticleAuthors(models.Model):
    article = models.ForeignKey(Article)
    author = models.ForeignKey(Author)
    position = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ('article','author','position')
        unique_together = ('article', 'author', 'position')
        index_together = [ ['article', 'author'], ]
