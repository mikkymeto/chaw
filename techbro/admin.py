from dis import show_code
from django.contrib import admin
from .models import Category, Dish, Showcase

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','cat_name', 'cat_image']
    list_editable = ['cat_name', 'cat_image']

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ['id','category_id','name','image','special','breakfast','lunch','dinner','drink','appetiser','dessert','price','min','max','in_stock']
    list_editable = ['special']
    

@admin.register(Showcase)
class ShowcasehAdmin(admin.ModelAdmin):
    list_display = ['id','show_name','show_txt','show_img']
    


# admin.site.register(Category,CategoryAdmin)
# admin.site.register(Dish,DishAdmin)