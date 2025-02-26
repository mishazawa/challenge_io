dev:
	docker compose -f docker-compose.prod.yml -f docker-compose.dev.yml up -d --build

run:
	docker compose -f docker-compose.prod.yml up -d --build

run-ec2:
	docker-compose -f docker-compose.prod.yml up -d --build

cleanup:
	rm -f .env.dev
	rm -f docker-compose.dev.yml
	rm -f Caddyfile.dev
