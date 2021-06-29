FROM python:alpine
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
WORKDIR /app
COPY . .
RUN apk --no-cache add git \           
            libreoffice \
            ttf-droid-nonlatin \
            ttf-droid \
            ttf-dejavu \
            ttf-freefont \
            ttf-liberation \        
        && rm -rf /var/cache/apk/* \
        && pip install -r requirements.txt \ 
        && git clone https://github.com/webodf/ViewerJS.git ./static/ViewerJS
EXPOSE 5000
CMD ["flask", "run"] 
