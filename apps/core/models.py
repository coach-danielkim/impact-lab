from django.db import models


class SiteSettings(models.Model):
    announcement_text = models.CharField(max_length=300, blank=True)
    announcement_active = models.BooleanField(default=False)
    announcement_link = models.URLField(blank=True)

    youtube_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    facebook_url = models.URLField(blank=True)
    thread_url = models.URLField(blank=True)

    address = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30, blank=True)

    class Meta:
        verbose_name = '사이트 설정'
        verbose_name_plural = '사이트 설정'

    def __str__(self):
        return 'Site Settings'

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class Partner(models.Model):
    name = models.CharField(max_length=100, verbose_name='파트너명')
    logo = models.ImageField(upload_to='partners/', blank=True, null=True, verbose_name='로고')
    url = models.URLField(blank=True, verbose_name='웹사이트')
    description = models.CharField(max_length=200, blank=True, verbose_name='설명')
    order = models.PositiveIntegerField(default=0, verbose_name='순서')
    is_active = models.BooleanField(default=True, verbose_name='활성화')

    class Meta:
        ordering = ['order']
        verbose_name = '파트너'
        verbose_name_plural = '파트너'

    def __str__(self):
        return self.name


class AdmissionResult(models.Model):
    CATEGORY_CHOICES = [
        ('ivy', 'IVY League'),
        ('top20', 'Top 20'),
        ('top50', 'Top 50'),
    ]
    year = models.PositiveIntegerField(verbose_name='연도')
    university = models.CharField(max_length=100, verbose_name='대학')
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, verbose_name='카테고리')
    count = models.PositiveIntegerField(default=1, verbose_name='합격 인원')
    is_featured = models.BooleanField(default=False, verbose_name='메인 노출')

    class Meta:
        ordering = ['-year', 'category']
        verbose_name = '합격 실적'
        verbose_name_plural = '합격 실적'

    def __str__(self):
        return f'{self.year} - {self.university}'


class Testimonial(models.Model):
    student_name = models.CharField(max_length=50, verbose_name='학생 이름')
    admitted_school = models.CharField(max_length=100, verbose_name='합격 학교')
    content = models.TextField(verbose_name='후기 내용')
    photo = models.ImageField(upload_to='testimonials/', blank=True, null=True, verbose_name='사진')
    year = models.PositiveIntegerField(verbose_name='연도')
    is_featured = models.BooleanField(default=False, verbose_name='메인 노출')
    order = models.PositiveIntegerField(default=0, verbose_name='순서')

    class Meta:
        ordering = ['order', '-year']
        verbose_name = '학생 후기'
        verbose_name_plural = '학생 후기'

    def __str__(self):
        return f'{self.student_name} - {self.admitted_school}'
