from django.contrib import admin

from .models import LiveMatch, FinishedMatch, Result

# Register your models here.
admin.site.register(LiveMatch)
admin.site.register(FinishedMatch)
admin.site.register(Result)
