FROM python:2.7-alpine
MAINTAINER dantebarba.alerts@gmail.com

COPY . .

RUN ["python", "setup.py", "install"]

ENV username=""
ENV password=""
ENV bonds='["AY24","DICA","AO20","AF20","A2E2"]'

EXPOSE 5000

CMD ["sh", "-c", "python -m cotizacion_mep $username $password $bonds"]