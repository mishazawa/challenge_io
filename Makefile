dev:
	docker compose -f docker-compose.prod.yml -f docker-compose.dev.yml up -d --build

run:
	docker compose -f docker-compose.prod.yml up -d --build