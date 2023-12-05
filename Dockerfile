FROM python:3.8

RUN mkdir /home/dev/ && mkdir /home/dev/code/

WORKDIR /home/dev/code/

# Exposez le port 8888
EXPOSE 8888:8888

#ENV http_proxy http://147.215.1.189:3128
#ENV https_proxy http://147.215.1.189:3128

COPY . .
RUN  pip install --upgrade pip &&  pip install pipenv && pipenv install --skip-lock && pip install jupyter && pip install notebook

CMD ["pipenv", "run", "jupyter", "notebook", "--ip=0.0.0.0", "--no-browser", "--allow-root", "--NotebookApp.token=''"]
#CMD ["/bin/bash"]
