make_migr:
	docker-compose run --rm rest_ex sh -c "python manage.py makemigrations bank"

migr:
	docker-compose run --rm rest_ex sh -c "python manage.py migrate"

ssh_w:
	docker-compose exec rest_ex sh

m_shell:
	docker-compose run --rm rest_ex sh -c "python manage.py shell"





