from django.conf import settings
from django.db import models
from django.utils import timezone



class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    LEAGUE = (
        ('PL', 'Premier League'),
        ('LL', 'La liga'),
        ('SA', 'Seria A'),
        ('L1', 'League 1'),
        ('CL', 'Champions league'),
        ('BL', 'Bundas league')
    )
    league = models.CharField(
        max_length=32,
        choices=LEAGUE,
        default='PL'
    )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



class MiniPost(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField()


	def __str__(self):
		return self.title

	


