from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField


class Article(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300)
    content = RichTextField(blank= True, null=True)
    # content = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('article_detail', kwargs={'pk': self.pk})
