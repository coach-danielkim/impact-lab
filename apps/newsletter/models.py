from django.db import models

class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True, verbose_name='이메일')
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = '뉴스레터 구독자'
        verbose_name_plural = '뉴스레터 구독자'

    def __str__(self):
        return self.email
