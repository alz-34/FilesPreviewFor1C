FROM python:3.9-rc-slim
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
WORKDIR /app
COPY requirements.txt .
RUN apt-get update \
    && apt-get install -y git unoconv \ 
    && apt-get clean \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/* \
    && pip install -r requirements.txt \ 
    && git clone https://github.com/webodf/ViewerJS_release.git ./static
RUN ln -s $(find /usr -name 'uno.py') /usr/lib/libreoffice/program/uno.py \
    && ln -s $(find /usr -name 'unohelper.py') /usr/lib/libreoffice/program/unohelper.py
COPY . .
CMD ["flask", "run"] 
