# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Quiz, QuizNow, Bingo, Score, RightWrong, Announcement

# Register your models here.
admin.site.register(Quiz)
admin.site.register(QuizNow)
admin.site.register(Bingo)
admin.site.register(Score)
admin.site.register(RightWrong)
admin.site.register(Announcement)
