import datetime

from django.db import models


class Author(models.Model): #автор
    name = models.CharField(
        max_length=300, verbose_name='Имя автора', help_text='Введите имя автора'
    )
    birth_date: datetime.date = models.DateField()

    def get_age(self) -> int:
        return (datetime.date.today() - self.birth_date).days // 365

    def set_age(self, age: int):
        self.birth_date = (
                datetime.date.today() - datetime.timedelta(days=365 * age))

    age = property(get_age, set_age)

    def __str__(self):
        return f'{self.name} ({self.age})'
