# Ngrok Port Forwarder

Forward a local port to a public URL using Ngrok.

## Overview

This project provides a Python script to forward a local port to a public URL using Ngrok. It allows developers to expose their local development environment to the world with ease.

## Features

- **Port Forwarding**: Forward a local port to a public URL using Ngrok.
- **Protocol Support**: Supports TCP and UDP protocols.
- **Optional Settings**: Optional authtoken, region, and binary path settings for customization.
- **Rich Console Interface**: Rich console interface for easy use.

## TODO:

- [ ] **Add Support for Multiple Protocols**: Implement support for multiple protocols simultaneously.

## Usage

### Installation

1. Clone the repository:

```bash
git clone https://github.com/real0x0a1/ngrok-port-forwarder.git
```

2. Install dependencies:

```bash
pip3 install -r requirements.txt
```

### Usage

1. Run the script `main.py`:

```bash
python3 main.py
```

2. Follow the prompts to enter the port, protocol, and optional settings.

## Configuration

You can set the following environment variables to customize the script:

- `NGROK_AUTHTOKEN`: your Ngrok authtoken
- `NGROK_REGION`: the Ngrok region to use (e.g. us, eu, etc.)
- `NGROK_BINARY_PATH`: the path to the Ngrok binary

## Acknowledgements

- [Ngrok](https://github.com/inconshreveable/ngrok)
- [Pyngrok](https://github.com/alexdlaird/pyngrok)
- [Rich](https://github.com/Textualize/rich)

## Contributing

Contributions are welcome! Fork the repository and submit a pull request.

## Issues

Please open an issue on the GitHub repository for any bugs or feature requests.

## Author

real0x0a1 (Ali)

---
