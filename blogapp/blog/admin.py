from django.contrib import admin
from .models import Blog, Category, BlogCity, TripCity
from django.utils.safestring import mark_safe


class BlogAdmin(admin.ModelAdmin):

    list_display = ("title", "is_home", "is_active", "slug", "selected_categories",)
    list_editable = ("is_active", "is_home",)
    search_fields = ("title", "description",)
    readonly_fields= ("slug",)
    list_filter = ("categories", "is_home", "is_active",)
    

    def selected_categories(self, obj):       #bloga ait secilen kategorinin admin panelinde gösterilmesi
        html = "<ul>" 

        for category in obj.categories.all():
            html += "<li>" + category.name + "</li>"

        html += "</ul>"

        return mark_safe(html)


admin.site.register(Blog, BlogAdmin)         #Bu kategorileri admin paneline ekledik
admin.site.register(Category)
admin.site.register(BlogCity)
admin.site.register(TripCity)
