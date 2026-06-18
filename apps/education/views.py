from django.shortcuts import render
from apps.core.models import Partner


def index(request):
    partners = Partner.objects.filter(is_active=True)
    return render(request, 'education/index.html', {'partners': partners})
