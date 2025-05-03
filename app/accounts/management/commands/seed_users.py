from email.policy import default

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Seeds the database with fake users'

    def add_arguments(self, parser):
        parser.add_argument('--count', type=int, default=10)

    def handle(self, *args, **kwargs):
        fake = Faker()
        count = kwargs['count']
        User = get_user_model()

        roles = ['doctor', 'patient', 'admin']

        for _ in range(count):
            role = random.choice(roles)
            is_staff = role in ['admin']

            email = fake.unique.email()
            password = 'testpass123'

            user = User.objects.create_user(
                email=email,
                password=password,
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                date_of_birth=fake.date_of_birth(minimum_age=18, maximum_age=65),
                phone_number=fake.phone_number(),
                street=fake.street_address(),
                postal_code=fake.postcode(),
                city=fake.city(),
                state=fake.state(),
                country=fake.country(),
                role=role,
                is_staff=is_staff
            )
            self.stdout.write(self.style.SUCCESS(f'Created {role} → {email} (is_staff={is_staff})'))