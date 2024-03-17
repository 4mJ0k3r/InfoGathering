# Info Gathering Tool

This is a basic information gathering tool written in Python. It retrieves WHOIS information, DNS records, and geolocation information for a given domain name.

## Features

- **WHOIS Lookup**: Retrieve registration information for a domain name using WHOIS lookup.
- **DNS Resolution**: Resolve DNS records (A, NS, MX, TXT) for a domain name.
- **Geolocation**: Fetch geolocation information based on the domain's IP address.

## Requirements

- Python 3.x
- Libraries:
    - `whois`: Library for WHOIS lookup.
    - `dns.resolver`: Library for DNS resolution.
    - `requests`: Library for making HTTP requests.
    - `socket`: Library for socket operations.
    - `argparse`: Library for parsing command-line arguments.

## Usage

