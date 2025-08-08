1. Download all the files and put them into one folder.
2. Run the Docker.
3. Open Powershell with the path to this folder.
4. Create the folder 'certs' by (e.g. by writing 'mkdir certs')
5. Type 'docker run --rm -v ${PWD}/certs:/certs alpine/openssl req -x509 -nodes -days 365 -newkey rsa:2048 -subj "/C=PL/ST=Test/L=Test/O=WeatherApp/CN=localhost" keyout /certs/key.pem -out /certs/cert.pem' in Powershell.
6. Type 'docker-compose up' in Powershell
7. Type 'https://localhost/weather/'.
8. You will see the data about the weather in this city.
