git clone https://github.com/mdtarhini/cheat-sheet-maker.git

# 用docker做image

docker build --rm -f "Dockerfile.product" --target product -t cheatsheet:v0.2 .


# 用docker compose做image

docker-compose build --force-rm --no-cache

docker-compose down
docker-compose up -d


