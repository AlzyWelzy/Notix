start:
	python manage.py runserver


celery:
	celery -A core worker --loglevel=info

celery-beat:
	celery -A core beat --loglevel=info

migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

venv:
	python -m venv .venv

install:
	pip install -r requirements.txt

clean:
	rm -rf .venv

freeze:
	pip freeze > requirements.txt

run:
	python manage.py runserver

shell:
	python manage.py shell

activate-mac:
	source ./.venv/bin/activate

activate:
	source .venv/bin/activate

deactivate:
	deactivate

