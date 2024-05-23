FROM python:3.10

RUN mkdir /crm

WORKDIR /crm

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY . .

RUN python manage.py migrate

RUN python manage.py collectstatic --noinput

RUN #chmod a+x /crm/docker/*.sh


CMD ["gunicorn", "reports_fintablo.wsgi:application", "--bind", "0.0.0.0:8000"]
