FROM alpine:3.15

RUN set -ex \
    && apk add --no-cache python3 tzdata \
    && ln -sfn /usr/share/zoneinfo/America/New_York /etc/localtime \
    && addgroup -S app && adduser -S -G app app 

ADD unifi_proxy.py packet.json /code/
WORKDIR /code

USER app

EXPOSE 10001

ENTRYPOINT [ "python3", "unifi_proxy.py" ]

