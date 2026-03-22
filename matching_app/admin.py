from django.contrib import admin
from .models import Candidate, Role, Match, Prediction

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'required_skills')
    search_fields = ('name',)

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('candidate', 'role', 'match_percentage', 'fit_category')
    list_filter = ('role', 'fit_category')

@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):
    list_display = ('candidate', 'top_role_1', 'score_1')
