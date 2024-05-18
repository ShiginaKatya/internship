from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
from .resource import *

class CategoryAdmin(ImportExportModelAdmin):
    resource_class = CategoryResource
admin.site.register(Category, CategoryAdmin)

class CompanyAdmin(ImportExportModelAdmin):
    resource_class = CompanyResource
admin.site.register(Company, CompanyAdmin)

class InternshipAdmin(ImportExportModelAdmin):
    resource_class = InternshipResource
admin.site.register(Internship, InternshipAdmin)

class Social_typeAdmin(ImportExportModelAdmin):
    resource_class = Social_typeResource
admin.site.register(Social_type, Social_typeAdmin)

class Social_mediaAdmin(ImportExportModelAdmin):
    resource_class = Social_mediaResource
admin.site.register(Social_media, Social_mediaAdmin)