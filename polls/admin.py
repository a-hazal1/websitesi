from django.contrib import admin

# Register your models here.

from polls.models import Category, Product, Images

class ProductImageInline(admin.TabularInline):
    model = Images
    readonly_fields = ('id',)
    extra = 5

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'parent']
    list_filter = ['status']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'amount', 'status']
    list_filter = ['status', 'category']
    inlines = [ProductImageInline]


class ImagesAdmin(admin.ModelAdmin):
    list_display = ['image','title','image_tag','product']
    readonly_fields = ('image_tag',)

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Images,ImagesAdmin)