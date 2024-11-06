from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Сохраняем уникальность поля email
    email = models.EmailField(unique=True)

    # Указываем, что аутентификация будет использовать поле email, а не username
    USERNAME_FIELD = 'email'
    
    # Если хотите, можете удалить поле username, так как оно уже не используется для аутентификации.
    REQUIRED_FIELDS = []  # Пустой список, так как email будет использоваться для аутентификации.

    def save(self, *args, **kwargs):
        # Убедитесь, что username не пустое, если не используете его, установите пустое значение
        if not self.username:
            self.username = self.email  # Используем email в качестве username, если оно пустое
        super().save(*args, **kwargs)
