release: python manage.py migrate
web: daphne expensinator.asgi:application  -t 60 --access-log - --port $PORT --bind 0.0.0.0 -v2 --proxy-headers
