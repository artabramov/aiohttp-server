build:
	docker build --no-cache -t hide-server .
	docker-compose up -d
