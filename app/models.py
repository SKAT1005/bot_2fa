from django.db import models

class User(models.Model):
    tg_id = models.IntegerField(verbose_name='ID пользователя в телеграмме')
    unique_id = models.CharField(max_length=64, verbose_name='Уникальный Id пользователя')
    code = models.IntegerField(default=0, verbose_name='Код 2fa')
    last_message = models.IntegerField(default=0, verbose_name='Последнее сообщение пользователя')
