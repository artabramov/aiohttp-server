docker build --no-cache -t hide-server .
# docker run -dit -p 80:80 --name hide-server hide-server
docker-compose up -d
