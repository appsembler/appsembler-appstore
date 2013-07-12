from django.db import models
from categories.models import CategoryBase


class Application(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey("AppCategory", related_name="applications")
    logo = models.ImageField(upload_to='app_logos')
    author = models.CharField(max_length=100, blank=True)
    version = models.CharField(max_length=15, blank=True)
    license_type = models.CharField(max_length=30, blank=True)
    website = models.URLField(blank=True)
    source_code_url = models.URLField(blank=True)
    demo_site_url = models.URLField(blank=True)

    def __unicode__(self):
        return self.name


class AppCategory(CategoryBase):
    description = models.TextField()

    class Meta:
        verbose_name_plural = "application categories"
