biuld:
	docker-compose up --build -d

run:
	docker-compose up -d

prepmigrations:
	docker exec -it iclinic_web sh -c "python manage.py makemigrations"

runmigrations:
	docker exec -it iclinic_web sh -c "python manage.py migrate"

test:
	docker-compose up -d
	docker exec -it iclinic_web sh -c "pip install -r requirements.txt"
	docker exec -it iclinic_web sh -c "coverage run manage.py test -v 2"
	docker exec -it iclinic_web sh -c "coverage html --omit='venv/*'"

superuser:
	docker exec -it iclinic_web sh -c "python manage.py createsuperuser"

dbflush:
	docker exec -it iclinic_web sh -c "python manage.py flush"

dbdump:
	docker exec -it iclinic_web sh -c "python manage.py dumpdata --format=json --indent=4 --database=default --all > db_dump.json"