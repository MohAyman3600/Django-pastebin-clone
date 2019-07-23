from django.db import models


class Snippet(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.title:
            return self.title
        else:
            return 'Snippet created at{}'.format(self.created_at)

    class Meta:
        ordering = ['created_at']
