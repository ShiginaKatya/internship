from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='название направления', max_length=255)
    

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Направление'
        verbose_name_plural = 'Направления'

class Company(models.Model):
    name = models.CharField(verbose_name='название компании', max_length=255)
    

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

class Internship(models.Model):
    company_id = models.ForeignKey(to=Company, on_delete=models.CASCADE, verbose_name='компания')
    description = models.TextField(verbose_name='описание стажировки', max_length=255)
    category_id = models.ForeignKey(to=Category, on_delete=models.CASCADE, verbose_name='направление')
    link = models.URLField(verbose_name='ссылка на сайт')
    recruitment = models.CharField(verbose_name='набор', max_length=255)

    def __str__(self):
        return self.company_id.name
    
    class Meta:
        verbose_name = 'Стажировка'
        verbose_name_plural = 'Стажировки'

class Social_type(models.Model):
    name = models.CharField(verbose_name='социальная сеть', max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Социальная сеть'
        verbose_name_plural = 'Социальные сети'

class Social_media(models.Model):
    company_id = models.ForeignKey(to=Company, on_delete=models.CASCADE, verbose_name='стажировка')
    type_id = models.ForeignKey(to=Social_type, on_delete=models.CASCADE, verbose_name='соцсеть')
    link = models.URLField(verbose_name='ссылка на соцсеть')
    def __str__(self):
        return self.link
    
    class Meta:
        verbose_name = 'Cсылка на соцсети'
        verbose_name_plural = 'Ссылки на соцсети'

