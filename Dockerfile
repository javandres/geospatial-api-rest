FROM python:3.7

#RUN adduser -D appuser
#RUN useradd -ms /bin/bash appuser

WORKDIR /usr/src

RUN pip install pip --upgrade
#RUN pip install setuptools --upgrade 

COPY requirements.txt requirements.txt
#RUN python -m venv venv
RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY app app
COPY run.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP run.py

#RUN chown -R appuser:appuser ./
#USER appuser

EXPOSE 4000
#ENTRYPOINT ["./boot.sh"]
#CMD ["gunicorn", "-b", "0.0.0.0:5000", "run"]
ENTRYPOINT [ "python" ]
CMD [ "run.py" ]