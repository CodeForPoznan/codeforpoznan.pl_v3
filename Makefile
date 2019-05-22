start:
	docker-compose up -d

logs:
	docker-compose logs

stop:
	docker-compose stop

populate_database:
	docker exec -ti codeforpoznanpl_v3_backend_1 flask populate-database
