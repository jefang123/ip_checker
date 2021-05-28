# ip_checker

This project sets up a small flask server that runs checks on given ip addresses against [this](https://raw.githubusercontent.com/stamparm/ipsum/master/levels/5.txt") ip list

The server only has a single endpoint `/checkips` that accepts `POST` requests with data in the following format:
```
{"ips":[ip1, ip2, ...]}
```

Requirements:
```
python 3.7+
pipenv
```

Run application:
```
pipenv install
pipenv run flask run
```

Test endpoint with curl:
```
curl -X POST http://localhost:5000/checkips -H "Content-Type: application/json" -d '{"ips":["94.142.241.194", "192.168.1.1"]}'
```

Run test suite.
```
python3 test.py
```

Running with docker
```
docker-compose up
```

## Notes
The source file ip validator in `ping.py` currently takes too long to set up synchronously, this should be run asynchronously to avoid connection errors during set up.