from django.contrib import admin
from .models import SiteSettings, Partner, AdmissionResult, Testimonial


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('공지 알림 바', {'fields': ('announcement_active', 'announcement_text', 'announcement_link')}),
        ('소셜 미디어', {'fields': ('youtube_url', 'linkedin_url', 'instagram_url', 'facebook_url', 'thread_url')}),
        ('연락처', {'fields': ('address', 'email', 'phone')}),
    )


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'order', 'is_active')
    list_editable = ('order', 'is_active')


@admin.register(AdmissionResult)
class AdmissionResultAdmin(admin.ModelAdmin):
    list_display = ('year', 'university', 'category', 'count', 'is_featured')
    list_filter = ('year', 'category')
    list_editable = ('is_featured',)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'admitted_school', 'year', 'is_featured', 'order')
    list_editable = ('is_featured', 'order')
