#!/bin/python3

# -*- Author: real0x0a1 (Ali) -*-
# -*- File: main.py -*-

# import libraries
import os

from pyngrok import ngrok
from rich.prompt import Prompt
from rich.console import Console
from rich.panel import Panel

console = Console()

def main():
    console.print(Panel.fit("[green]Ngrok Port Forwarder\nBy:   [red]real0x0a1[/][/]", title="[blue]Welcome[/]"))

    # Ask for the port to forward
    port = Prompt.ask("[cyan]Enter the port to forward[/]", default="8080")

    # Ask for the protocol (tcp, udp, etc.)
    protocol = Prompt.ask("[cyan]Enter the protocol (http, tcp, udp, etc.)[/]", default="http")

    # Set the authtoken (optional)
    ngrok_authtoken = os.environ.get("NGROK_AUTHTOKEN")
    if ngrok_authtoken:
        ngrok.conf.get_default().auth_token = ngrok_authtoken
        console.print(f"Using authtoken: {ngrok_authtoken}", style="green")

    # Set the region (optional)
    ngrok_region = os.environ.get("NGROK_REGION")
    if ngrok_region:
        ngrok.conf.get_default().region = ngrok_region
        console.print(f"Using region: {ngrok_region}", style="green")

    # Set the binary path (optional)
    ngrok_binary_path = os.environ.get("NGROK_BINARY_PATH")
    if ngrok_binary_path:
        ngrok.conf.get_default().ngrok_path = ngrok_binary_path
        console.print(f"Using binary path: {ngrok_binary_path}", style="green")

    # Start the ngrok tunnel
    ngrok_tunnel = ngrok.connect(int(port), protocol)
    console.print(f"Ngrok tunnel started on port {port} with protocol {protocol}", style="green")

    # Print the public URL
    console.print(f"Public URL: {ngrok_tunnel.public_url}", style="blue")

    # Keep the tunnel running
    console.print("Press Ctrl+C to stop the tunnel", style="yellow")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        console.print("Stopping ngrok tunnel...", style="red")
        ngrok_tunnel.close()
        console.print("Ngrok tunnel stopped", style="red")

if __name__ == "__main__":
    main()
