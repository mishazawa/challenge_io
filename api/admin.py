from django.contrib import admin
from .models import User, Challenge, Submission, Participation

# Register your models here.
admin.site.register([User, Challenge, Submission, Participation])
