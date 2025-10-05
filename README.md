# ElectrumX with Palladium (PLM) Support

This repository provides a **Dockerized** setup of **ElectrumX** with support for the **Palladium (PLM)** coin.
It also includes a test script (`test-server.py`) to verify the connection and main functionalities of the ElectrumX server.

Tested on:

* ✅ Debian 12
* ✅ Ubuntu 24.04

🔗 Palladium Full Node: [NotRin7/Palladium](https://github.com/NotRin7/Palladium)

---

## Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Electrum      │    │   ElectrumX     │    │   Palladium     │
│   Clients       │◄──►│   Server        │◄──►│   Full Node     │
│                 │    │   (Docker)      │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

---

## Requirements

* [Docker](https://docs.docker.com/get-docker/)
* [Docker Compose](https://docs.docker.com/compose/install/)
* Python 3.10+ (to use `test-server.py`)
* A running **Palladium** full node ([NotRin7/Palladium](https://github.com/NotRin7/Palladium))

**System Architecture**: This server requires a **64-bit system** (both AMD64 and ARM64 architectures are supported, but 32-bit systems are not compatible).

**Recommendation**: to ensure maximum stability and reduce communication latency, it is strongly recommended to run the Palladium node **on the same machine** that hosts the ElectrumX container.

---

## Docker Installation

If you don't have Docker installed yet, follow the official guide:
- [Install Docker](https://docs.docker.com/get-docker/)

For Docker Compose:
- [Install Docker Compose](https://docs.docker.com/compose/install/)

---

## Configuration

In the `docker-compose.yml` file, you can set the RPC credentials of the Palladium full node that ElectrumX will use:

```yaml
environment:
  - DAEMON_URL=http://<rpcuser>:<rpcpassword>@<host>:<port>/
```

Replace with your actual values:

* `<rpcuser>` → RPC username of the node
* `<rpcpassword>` → RPC password of the node
* `<host>` → node address (e.g., `127.0.0.1`)
* `<port>` → RPC port of the node (e.g., `2332` for Palladium)

**Important:** never include real credentials in files you upload to GitHub.

---

## Build and Start the Project

1. Navigate to the directory containing `docker-compose.yml` and `Dockerfile`.

2. Build the custom Docker image:

   ```bash
   docker build -t electrumx-plm:local .
   ```

3. Start the containers with Docker Compose:

   ```bash
   docker compose up -d
   ```

4. Check the logs to verify that ElectrumX started correctly:

   ```bash
   docker compose logs -f
   ```
---

## Testing with `test-server.py`

The `test-server.py` script allows you to connect to the ElectrumX server and test its APIs.

Usage example:

```bash
python test-server.py 127.0.0.1:50002
```

The script will perform:

* Handshake (`server.version`)
* Feature request (`server.features`)
* Block header subscription (`blockchain.headers.subscribe`)

---

## Notes

* `coins_plm.py` defines the **Palladium (PLM)** coin, based on Bitcoin.
* Production recommendations:

  * Protect RPC credentials
  * Use valid SSL certificates
  * Monitor containers (logs, metrics, alerts)

---

## License

Distributed under the **MIT** license. See the `LICENSE` file for details.
