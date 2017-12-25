FROM python

MAINTAINER TimWells "1807520300@qq.com"

COPY * /home/blogproject/

WORKDIR /home/blogproject

RUN pip install -i https://pypi.douban.com/simple/ -r build/requirements.txt

WORKDIR /home/blogproject/project

RUN python manage.py collectstatic --noinput

RUN python manage.py makemigrations

RUN python manage.py migrate

CMD gunicorn -c gun.py blogproject.wsgi:application