for migrate:
docker/bin/python manage.py migrate

for makemigrations:
docker/bin/python manage.py makemigrations

for edit files:
sudo chown -hR nilu:nilu .

for create superuser:
docker/bin/python manage.py createsuperuser

Load fixture:
docker/bin/python manage.py migrate
docker/bin/python manage.py makemigrations
docker/bin/python manage.py loaddata accounts/fixtures/test_users.json

to hash a password in shell:
docker/bin/python manage.py shell
and then:
from django.contrib.auth.hashers import make_password
make_password('testpass')


to finde group's name in shell:
docker/bin/python manage.py shell
and then:
from django.contrib.auth.models import Group

for group in Group.objects.all():
    print(group.id, group.name)
then we have this:
3 superadmin
4 admin

to install something:
docker/bin/pip install ....
# docker-compose exec web pip install .....

for seed_users:
docker/bin/python manage.py seed_users --count 5
or:
docker/bin/python manage.py seed_users