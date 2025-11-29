from django.contrib import admin
from . models import MediaAsset

# Register your models here.
@admin.register(MediaAsset)
class MediaAssetAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'uploaded_by', 'created_at', 'is_public', 'views_count')
    list_filter = ('category', 'is_public', 'created_at', 'uploaded_by')
    search_fields = ('title', 'description', 'uploaded_by__username')
    readonly_fields = ('views_count','created_at','updated_at') 
    date_hierarchy = 'created_at'# to navigate records by date
    ordering = ('-created_at',)
