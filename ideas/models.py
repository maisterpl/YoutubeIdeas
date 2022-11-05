from django.db import models

# Create your models here.
class Idea(models.Model):
    IDEA_STATUS = (
        ('pending', 'Waiting for review'),
        ('accepted', 'Accepted'),
        ('done', 'Done'),
        ('rejected', 'Rejected')
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    youtube_url = models.URLField(null=True, blank=True)
    status = models.CharField(max_length=30, choices=IDEA_STATUS, default='status_pending')

    def __str__(self) -> str:
        return self.title


class Vote(models.Model):
    # idea is provide a may to one and when we delete idea we delete all votes
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    reason = models.TextField()

    def __str__(self) -> str:
        return f'Vote ID {self.id}'