from django.contrib import admin
from .models import Exam, Question, Option, Quiz

class OptionInline(admin.TabularInline):
    model = Option

class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]

class QuizAdmin(admin.ModelAdmin):
    filter_horizontal = ('questions',)

admin.site.register(Exam)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Quiz, QuizAdmin)
