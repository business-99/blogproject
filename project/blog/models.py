from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.six import python_2_unicode_compatible


@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=24, verbose_name='分类')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=24, verbose_name='标签')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField(max_length=32, verbose_name='博文')
    excerpt = models.CharField(max_length=124, blank=True, verbose_name='概要')
    source_url = models.URLField(verbose_name='引文地址', null=True, blank=True, help_text='options')
    content = models.TextField(verbose_name='内容')
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    modified_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    category = models.ForeignKey(Category, verbose_name='分类')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='标签')
    author = models.ForeignKey(User, verbose_name='作者', default=1)
    view_times = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def increase_views(self):
        self.view_times += 1
        self.save(update_fields=['view_times'])

    def save(self, *args, **kwargs):
        self.excerpt = self.content[:108]
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_time', 'view_times']
