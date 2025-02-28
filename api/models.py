import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Challenge(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    start_date = models.DateField()
    end_date = models.DateField()

    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    participants = models.ManyToManyField(
        User, through="Participation", related_name="challenges"
    )

    def __str__(self):
        return self.title


class Submission(models.Model):
    submission_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.SET_NULL, null=True)
    description = models.TextField()

    def __str__(self):
        return f"Submission {self.submission_id} from {self.owner.username} in {self.challenge.title}"


class Participation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} participate {self.challenge.title} since {self.joined_at}"
