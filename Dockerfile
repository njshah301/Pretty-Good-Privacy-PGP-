FROM python

WORKDIR /user/PGP


COPY ./ ./
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt


RUN python


CMD ["python","main.py"]