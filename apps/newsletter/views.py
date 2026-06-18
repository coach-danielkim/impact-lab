from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import NewsletterSubscriber

@require_POST
def subscribe(request):
    email = request.POST.get('email', '').strip()
    if not email:
        return JsonResponse({'success': False, 'message': '이메일을 입력해주세요.'})
    _, created = NewsletterSubscriber.objects.get_or_create(email=email)
    if created:
        return JsonResponse({'success': True, 'message': '구독해 주셔서 감사합니다!'})
    return JsonResponse({'success': True, 'message': '이미 구독 중인 이메일입니다.'})
