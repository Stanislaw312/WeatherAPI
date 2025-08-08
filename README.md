Download all the files and put them into one folder.
Run the Docker.
Open Powershell with the path to this folder.
Type 'docker run --rm -v ${PWD}/certs:/certs alpine/openssl req -x509 -nodes -days 365 -newkey rsa:2048 -subj "/C=PL/ST=Test/L=Test/O=WeatherApp/CN=localhost" -keyout /certs/key.pem -out /certs/cert.pem' in Powershell.
Type 'docker-compose up' in Powershell
Type 'https://localhost/weather/'.
You will see the data about the weather in this city.
