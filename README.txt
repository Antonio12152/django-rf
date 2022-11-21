python -m pip install --upgrade pip
pip install django djangorestframework
django-admin startproject drfsite
cd drfsite
python manage.py migrate
python manage.py startapp blog


аутентификация по токенам
pip install djoser
http://127.0.0.1:8000/auth/token/login
414addebfa86523d63f6d5c1230ad4eba705be4f
http://127.0.0.1:8000/auth/token/logout/
