FROM python:3.10-slim

ADD ./ /opt/otree
ADD ./entrypoint.sh /entrypoint.sh
ADD ./pg_ping.py /pg_ping.py
ADD ./requirements.txt /opt/otree/requirements.txt

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
     bash \
     curl \
     gcc \
     build-essential \
     python3-dev \
     libssl-dev \
     pkg-config \
     libpq-dev \
     libffi-dev \
     postgresql-client \
     rustc \
     cargo \
 && pip install --no-cache-dir -r /opt/otree/requirements.txt \
 && mkdir -p /opt/init \
 && pip3 uninstall -y uvicorn || true \
 && pip3 uninstall -y uvloop || true \
 && chmod +x /entrypoint.sh \
 && apt-get purge -y --auto-remove \
     gcc \
     build-essential \
     python3-dev \
     libssl-dev \
     pkg-config \
     libpq-dev \
     libffi-dev \
     rustc \
     cargo \
 && pip3 install --upgrade "uvicorn[standard]>=0.18.0,<1.0.0" \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/otree
VOLUME /opt/init
ENTRYPOINT ["bash", "/entrypoint.sh"]
CMD ["otree", "runprodserver", "--port=80"]
EXPOSE 80
