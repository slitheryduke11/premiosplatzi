from django.contrib import admin

from .models import Choice, Question


admin.site.register(Question)

# class ChoicesInline(admin.StackedInline):
#     model = Choice
#     can_delete = False
#     verbose_name_plural = 'choices'

# @admin.register(Question)
# class QuestionAdmin(admin.ModelAdmin):
#     inlines = (ChoicesInline,)




# class ChoiceAdmin(admin.ModelAdmin):
#     readonly_fields = ['votes']  # Campos de solo lectura

# admin.site.register(Choice, ChoiceAdmin)