from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['question_text', 'pub_date',]
    fieldsets = [
        ('Text', {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}), # 'classes': ['collapse']
        # ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}), # 'classes': ['collapse']
    ]
    # inlines = [ChoiceInline]
    # list_display = ('question_text', 'pub_date')
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date', 'question_text']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)

class ChoiceAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Votes', {'fields': ['votes']}),
        ('Question', {'fields': ['question']}),
        ('Choice Text', {'fields': ['choice_text']}),
    ]
    # fields = ['votes', 'choice_text', 'question']

admin.site.register(Choice, ChoiceAdmin)
# admin.site.register(Choice)
