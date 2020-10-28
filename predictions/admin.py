from django.contrib import admin

from .models import HistoricalData

# Register your models here.
class HistoricalDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'case_of', 'name', 'age', 'gender', 'case_reg_date', 'predicted_disease')
    list_display_links = ('id',)
    list_filter = ('case_of', 'age', 'gender', 'symptom_1', 'symptom_2', 'symptom_3', 'symptom_4', 'symptom_5')
    search_fields = ('id', 'case_of', 'name', 'age', 'gender', 'case_reg_date', 'symptom_1', 'symptom_2', 'symptom_3', 'symptom_4', 'symptom_5', 'predicted_disease')
    list_per_page = 25

admin.site.register(HistoricalData, HistoricalDataAdmin)