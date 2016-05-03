from apps.catalog.models import Category


def add_categories(request):
    return {'menu_categories': Category.objects.filter(level=0)}
