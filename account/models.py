from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email=None, first_name=None, last_name=None, phone_number=None, date_of_birth=None, password=None):
        # if not email:
        #     raise ValueError("Пользователи должны иметь email адрес")

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
        )
        objects = CustomUserManager()

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
            user = self.create_user(
                username=username,
                password=password,
                email="nurailymzhanyrbai19@gmail.com",
                first_name="nurailym",
                last_name="Zhanbyrbai",
                phone_number="+77777888990",
                date_of_birth="2003-07-19",
            )

            user.is_admin = True
            user.save(using=self._db)

            return user

class CustomUser(AbstractBaseUser):
    username = models.CharField("Логин пользователя", max_length=255, unique=True)

    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )

    date_of_birth = models.DateField()

    first_name = models.CharField("Имя пользователя", max_length=255)

    last_name = models.CharField("Фамилия пользователя", max_length=255)

    phone_number = models.CharField("Телефон", max_length=255)

    is_active = models.BooleanField(default=True)

    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin