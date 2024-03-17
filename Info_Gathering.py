# Import required libraries
import whois           # Library for WHOIS lookup
import dns.resolver    # Library for DNS resolution
import argparse        # Library for parsing command-line arguments
import requests        # Library for making HTTP requests
import socket          # Library for socket operations
import sys             # Library for system-specific parameters and functions

# Create ArgumentParser object for parsing command-line arguments
parser = argparse.ArgumentParser(description="This is a basic info-gathering tool", usage='python info_gathering.py -d DOMAIN ')
# Define command-line arguments
parser.add_argument("-d", "--domain", help="Enter the domain name for footprinting.")
parser.add_argument("-o", "--output", help="Enter the file name to write output to.")

# Parse the command-line arguments
args = parser.parse_args()

# Extract domain and output file name from command-line arguments
domain = args.domain
output_file = args.output

# Check if the output file name is provided
if output_file is None:
    print("Please provide an output file name using the -o or --output option.")
    sys.exit(1)  # Exit the script with a non-zero status code to indicate an error

# Initialize variables to store results
whois_result = ""
dns_result = ""
geo_result = ""

# Implementing WHOIS module
print("[+] WHOIS info found..")
whois_info = whois.whois(domain)
# Store WHOIS information in a string variable
whois_result += "Name: {}\n".format(whois_info.name)
whois_result += "Registrar: {}\n".format(whois_info.registrar)
whois_result += "Creation Date: {}\n".format(whois_info.creation_date)
whois_result += "Expiration Date: {}\n".format(whois_info.expiration_date)
# Print WHOIS information
print(whois_result)

#DNS Module
print("[+] Getting DNS info..")
try:
    # Resolve 'A' records (IPv4 addresses) for the domain
    for a in dns.resolver.resolve(domain, 'A'):
        dns_result += "[+] A Record: {}\n".format(a.to_text())

    # Resolve 'NS' records (name server records) for the domain
    for ns in dns.resolver.resolve(domain, 'NS'):
        dns_result += "[+] NS Record: {}\n".format(ns.to_text())

    # Resolve 'MX' records (mail exchange records) for the domain
    for mx in dns.resolver.resolve(domain, 'MX'):
        dns_result += "[+] MX Record: {}\n".format(mx.to_text())

    # Resolve 'TXT' records (text records) for the domain
    for txt in dns.resolver.resolve(domain, 'TXT'):
        dns_result += "[+] TXT Record: {}\n".format(txt.to_text())

except dns.resolver.NoAnswer:
    dns_result += "[-] No DNS records found for the domain.\n"
except dns.resolver.NXDOMAIN:
    dns_result += "[-] The domain does not exist.\n"
except dns.resolver.Timeout:
    dns_result += "[-] DNS resolution timed out.\n"
except dns.resolver.ResolverError as e:
    dns_result += "[-] DNS resolution error: {}\n".format(e)
except Exception as e:
    dns_result += "[-] An unexpected error occurred during DNS resolution: {}\n".format(e)

# Print DNS information
print(dns_result)

# Geolocation Module
print("[+] Getting geolocation info..")
try:
    # Make a request to geolocation API to get information based on the domain's IP address
    response = requests.request('GET',"https://geolocation-db.com/json/" + socket.gethostbyname(domain)).json()
    # Store geolocation information in a string variable
    geo_result += "[+] Country: {}\n".format(response['country_name'])
    geo_result += "[+] Latitude: {}\n".format(response['latitude'])
    geo_result += "[+] Longitude: {}\n".format(response['longitude'])
    geo_result += "[+] City: {}\n".format(response['city'])
    geo_result += "[+] State: {}\n".format(response['state'])
except Exception as e:
    geo_result += "Error: {}\n".format(e)

# Print geolocation information
print(geo_result)

# Write results to the output file
with open(output_file, 'w') as file:
    file.write("WHOIS Information:\n")
    file.write(whois_result)
    file.write("\n\n")
    file.write("DNS Information:\n")
    file.write(dns_result)
    file.write("\n\n")
    file.write("Geolocation Information:\n")
    file.write(geo_result)
    file.write("\n")
