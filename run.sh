docker build --no-cache -t hide-server .
# docker run -dit -p 80:80 -p 8080:8080 --name hide-server hide-server
docker-compose up -d
