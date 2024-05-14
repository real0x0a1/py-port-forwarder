# Ngrok Port Forwarder

A simple Python script to forward a local port to a public URL using Ngrok.

**Features**

- Forward a local port to a public URL using Ngrok
- Supports TCP and UDP protocols
- Optional authtoken, region, and binary path settings
- Rich console interface for easy use

**Getting Started**

1. Install the required dependencies: `pip3 install -r requirements.txt`
2. Download or clone this repository
3. Run the script: `python3 main.py`
4. Follow the prompts to enter the port, protocol, and optional settings

**Usage**

- Enter the port to forward (e.g. 8080)
- Enter the protocol (e.g. tcp or udp)
- Optional: enter the authtoken, region, and binary path settings
- The script will start the Ngrok tunnel and print the public URL
- Press Ctrl+C to stop the tunnel and exit the script

**Configuration**

You can set the following environment variables to customize the script:

- `NGROK_AUTHTOKEN`: your Ngrok authtoken
- `NGROK_REGION`: the Ngrok region to use (e.g. us, eu, etc.)
- `NGROK_BINARY_PATH`: the path to the Ngrok binary

**Contributing**

Contributions are welcome! If you'd like to add new features or fix bugs, please open a pull request.

**Acknowledgments**

This script uses the following libraries:

- Pyngrok: a Python wrapper for Ngrok
- Rich: a Python library for rich text formatting

**Author**

---
