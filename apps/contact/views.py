from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import ConsultationRequest


def index(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        consultation_type = request.POST.get('consultation_type', 'other')
        grade = request.POST.get('grade', '').strip()
        preferred_date = request.POST.get('preferred_date') or None
        message_text = request.POST.get('message', '').strip()

        if name and email and message_text:
            obj = ConsultationRequest.objects.create(
                name=name,
                email=email,
                phone=phone,
                consultation_type=consultation_type,
                grade=grade,
                preferred_date=preferred_date,
                message=message_text,
            )
            try:
                send_mail(
                    subject=f'[Impact Lab] 상담 신청 - {name}',
                    message=f'이름: {name}\n이메일: {email}\n연락처: {phone}\n유형: {obj.get_consultation_type_display()}\n학년: {grade}\n날짜: {preferred_date}\n\n{message_text}',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.ADMIN_EMAIL],
                    fail_silently=True,
                )
            except Exception:
                pass
            messages.success(request, '상담 신청이 완료되었습니다. 빠른 시일 내에 연락드리겠습니다.')
            return redirect('contact')
        else:
            messages.error(request, '이름, 이메일, 문의 내용은 필수 항목입니다.')

    return render(request, 'contact/index.html')
