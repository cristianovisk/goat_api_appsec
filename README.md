# API Goat Test
## CLI Run
```sh
python3 -v venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 run.py
```

## Docker Environment
```sh
git clone https://github.com/cristianovisk/goat_api_appsec.git
docker build -t api_goat:latest .
docker run --rm -d -p 8080:8080 api_goat:latest
curl http://127.0.0.1:8080/openapi.json
```