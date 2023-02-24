# Build with:
#     docker build -t qmh .
#
# Run it:
#     docker run -it -e DEBUG=1 -e SECRET_KEY=abcdefg qmh
#
# Local development (mount your local codebase):
#     docker run -it -e DEBUG=1 -e SECRET_KEY=abcdefg -v $(pwd):/app q,h

FROM python:3.11

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY . /app

RUN SECRET_KEY=1 python myAsylum/manage.py collectstatic --noinput --clear

EXPOSE 8000

CMD python myAsylum/manage.py runserver 0.0.0.0:8000
