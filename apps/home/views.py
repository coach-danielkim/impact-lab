from django.shortcuts import render
from apps.core.models import Partner, AdmissionResult, Testimonial


def index(request):
    partners = Partner.objects.filter(is_active=True)
    testimonials = Testimonial.objects.filter(is_featured=True)[:6]
    stats = {
        'ivy_count': AdmissionResult.objects.filter(category='ivy').count(),
        'top20_count': AdmissionResult.objects.filter(category='top20').count(),
        'years': 15,
        'students': 500,
    }
    return render(request, 'home/index.html', {
        'partners': partners,
        'testimonials': testimonials,
        'stats': stats,
    })
