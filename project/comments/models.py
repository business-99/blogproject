from django.db import models


class Comment(models.Model):
    name = models.CharField(max_length=16, default='anonymous')
    email = models.EmailField(max_length=32)
    url = models.URLField(blank=True, null=True, help_text='options')
    text = models.TextField(max_length=1024, help_text='评论内容...', verbose_name='评论')
    created_time = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('blog.Post')

    def __str__(self):
        return self.text[:20]

    class Meta:
        ordering = ['-created_time']
