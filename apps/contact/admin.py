from django.contrib import admin
from .models import ConsultationRequest


@admin.register(ConsultationRequest)
class ConsultationRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'consultation_type', 'preferred_date', 'status', 'created_at')
    list_filter = ('consultation_type', 'status', 'created_at')
    list_editable = ('status',)
    search_fields = ('name', 'email')
    readonly_fields = ('created_at',)
