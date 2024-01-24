docker build --no-cache -t hide-server .

# make run
docker run -dit --name hide-server hide-server
