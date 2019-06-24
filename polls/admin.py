from django.contrib import admin

from .models import Question

# set the Question table to be accessed thru the admin
admin.site.register(Question)