Инструкции по запуску:

Для создания контейнера в docker нужно набрать в консоли следующие команды:

docker network create drf_net

docker run -d --network=drf_net --name=postgres_container -p 5432:5432 -e POSTGRES_DB=dockerDRF -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=12345 postgres:latest

docker-compose up -d --build
