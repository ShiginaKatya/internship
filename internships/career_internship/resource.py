from import_export import resources 
from .models import *

class CategoryResource(resources.ModelResource):
     class Meta:
         model = Category

class CompanyResource(resources.ModelResource):
     class Meta:
         model = Company

class InternshipResource(resources.ModelResource):
     class Meta:
         model = Internship

class Social_typeResource(resources.ModelResource):
     class Meta:
         model = Social_type

class Social_mediaResource(resources.ModelResource):
     class Meta:
         model = Social_media