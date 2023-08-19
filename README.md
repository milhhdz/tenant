# RUN DOCKER COMPOSE
```
docker compose -f file.yml -p name_project up -d
```

# START PROJECT
## step 1
```
pip install virtualenv
```

## step 2
```
virtualenv env
```
## step 2.1
Linux
```
source venv/bin/activate
```
Win
```
.\venv\Scripts\activate
```

## step 3
```
pip install -r requirements.txt
```

## step 4
```
python3 manage.py migrate_schemas
```

## step 5
```
python3 manage.py runserver
```

localhost:8000