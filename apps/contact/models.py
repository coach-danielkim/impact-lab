from django.db import models


class ConsultationRequest(models.Model):
    TYPE_CHOICES = [
        ('admissions', '입시 컨설팅'),
        ('ai_lab', 'AI Lab'),
        ('veritas', '논술'),
        ('other', '기타'),
    ]
    STATUS_CHOICES = [
        ('received', '접수'),
        ('confirmed', '확인'),
        ('completed', '완료'),
    ]

    name = models.CharField(max_length=50, verbose_name='이름')
    email = models.EmailField(verbose_name='이메일')
    phone = models.CharField(max_length=20, blank=True, verbose_name='연락처')
    consultation_type = models.CharField(max_length=20, choices=TYPE_CHOICES, verbose_name='상담 유형')
    grade = models.CharField(max_length=20, blank=True, verbose_name='학년')
    preferred_date = models.DateField(null=True, blank=True, verbose_name='희망 상담 날짜')
    message = models.TextField(verbose_name='문의 내용')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='received', verbose_name='상태')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='신청일')

    class Meta:
        ordering = ['-created_at']
        verbose_name = '상담 신청'
        verbose_name_plural = '상담 신청'

    def __str__(self):
        return f'{self.name} - {self.get_consultation_type_display()} ({self.created_at.strftime("%Y-%m-%d")})'
