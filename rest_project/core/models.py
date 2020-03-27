from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Application(models.Model):
    """
    Модель приложения хранит в себе внешние источники,
    которые будут обращаться к API.
    """

    is_active = models.BooleanField('Активно', default=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='applications'
    )
    name = models.CharField('название приложения', max_length=255)
    api_key = models.CharField('ключ API', max_length=255)

    class Meta:

        verbose_name = "Приложение"
        verbose_name_plural = "Приложения"

    def __str__(self) -> str:
        return str(self.name)
