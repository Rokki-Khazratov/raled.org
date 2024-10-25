from django.contrib import admin

from api.models import *

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Social_media)
admin.site.register(History)



@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']  # Отображаемые поля в списке новостей
    search_fields = ['title', 'discription']  # Поля для поиска
    list_filter = ['created_at']  # Фильтр по дате создания
    ordering = ['-created_at']  # Сортировка по дате создания
    date_hierarchy = 'created_at'  # Добавление навигации по датам

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'work_place']  # Отображаемые поля в списке членов
    search_fields = ['name', 'work_place', 'discription']  # Поля для поиска
    list_filter = ['work_place']  # Фильтрация по месту работы
    ordering = ['name']  # Сортировка по имени

@admin.register(BookOrder)
class BookOrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'book_name', 'phone', 'created_at']  # Отображаемые поля в списке заказов
    search_fields = ['name', 'phone', 'book_name']  # Поля для поиска
    list_filter = ['created_at']  # Фильтр по дате создания
    ordering = ['-created_at']  # Сортировка по дате создания
    readonly_fields = ['created_at']  # Поле только для чтения
