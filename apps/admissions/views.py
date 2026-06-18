from django.shortcuts import render
from apps.core.models import AdmissionResult, Testimonial


def index(request):
    results = AdmissionResult.objects.all().order_by('-year', 'category')
    testimonials = Testimonial.objects.filter(is_featured=True)[:4]
    return render(request, 'admissions/index.html', {
        'results': results,
        'testimonials': testimonials,
    })
