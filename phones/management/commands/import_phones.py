import csv
from django.core.management.base import BaseCommand
from phones.models import Phone
from traceback import print_tb


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            # # TODO: Добавьте сохранение модели
            # obj = dict()

            Phone.objects.create(
                                name=phone['name'],
                                image=phone['image'],
                                price=phone['price'],
                                release_date=phone['release_date'], 
                                lte_exists=phone['lte_exists'],
            )
