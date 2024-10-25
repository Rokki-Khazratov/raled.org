from django.template import Library
from api.models import Product, Member

register = Library()


@register.filter()
def check_lang(request, obj: Member) -> bool:
    data = {
        'uz': obj.work_place_uz,
        'ru': obj.work_place_ru,
        'en': obj.work_place_en
    }   
    lang = request.path.split('/')[1]

    return data[lang]

