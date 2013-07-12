from django.db import models


class Application(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.ImageField(upload_to='app_logos')
    author = models.CharField(max_length=100, blank=True)
    version = models.CharField(max_length=15, blank=True)
    license_type = models.CharField(max_length=30, blank=True)
    website = models.URLField(blank=True)
    source_code_url = models.URLField(blank=True)
    demo_site_url = models.URLField(blank=True)

    def __unicode__(self):
        return self.name
