from django.contrib.admin import ModelAdmin, site

from clothing.models import TypeModel, ClothingModel

#how to admin category
class CategoryAdmin(ModelAdmin):
    list_display = ("id", "name")
    
    #display name and id as link to edit clothing
    list_display_links = ("id", "name")

#how to admin product
class ProductAdmin(ModelAdmin):
    list_display = ("manufacturer", "price", "type")

#connect between admin models
site.register(TypeModel, CategoryAdmin)
site.register(ClothingModel, ProductAdmin)