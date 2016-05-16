from apps.catalog.models import Category
from apps.home.models import Featured


def extra_context(request):
    return {
        'featured': Featured.objects.all(),
        'menu_categories': Category.objects.filter(level=0)
    }
