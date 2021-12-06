# unifi-proxy

Unifi Proxy for hosting Protect on a separate vlan.

1. Build docker-image:

    ```sh
    docker build --no-cache -t unifiproxy:latest .
    ```

1. Capture `packet.json`. You need a computer connected to the same vlan as Protect, as well as device which will attempt to connect to the Protect.

 FIXME

1. Start docker-compose in a container facing non-Protect vlan:

    ```sh
    docker-compose up -d
    ```
