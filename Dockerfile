FROM python:3.11-slim

RUN apt-get update \
&& apt-get install -y git \
&& rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["bash", "start.sh"]
