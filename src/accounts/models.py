from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("У пользователя должен быть \
            адрес электронной почты")
        user = self.model(
            email=self.normalize_email(email))

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    first_name = models.CharField(max_length=50, blank=False,
                                  verbose_name='Имя',
                                  help_text='Введите имя автора')
    last_name = models.CharField(max_length=100, blank=False,
                                 verbose_name='Фамилия',
                                 help_text='Введите фамилию автора')
    middle_name = models.CharField(max_length=50, blank=True,
                                   verbose_name='Отчество',
                                   help_text='Введите отчество автора')
    avatar = models.ImageField(upload_to='photo/avatars/%Y/%m/%d/',
                               blank=True, verbose_name='Аватар')
    created = models.DateField(auto_now_add=True,
                               verbose_name='Дата создания')
    date_of_birth = models.DateField(blank=False, null=True,  #как убрать null
                                     verbose_name='Дата рождения')
    slug = models.SlugField(max_length=255, unique=False, db_index=True, #как включить unique
                            verbose_name='URL')

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
