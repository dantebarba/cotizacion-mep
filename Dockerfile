FROM python:2.7-alpine
MAINTAINER dantebarba.alerts@gmail.com

COPY . .

RUN ["python", "setup.py", "install"]

ENV username=""
ENV password=""
ENV bonds='["AY24","DICA","AO20","AF20","A2E2","PARY","CO26","DICY","A2E8","AA25","AA37","AC17"]'

RUN ["python", "-m", "unittest", "discover", "tests"]

EXPOSE 5000

CMD ["sh", "-c", "python -m cotizacion_mep $username $password $bonds"]