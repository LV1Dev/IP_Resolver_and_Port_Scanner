import socket

def resolve_ip(domain_name):
    try:
        ip_address = socket.gethostbyname(domain_name)
        return ip_address
    except socket.gaierror as e:
        return f"Error: Unable to resolve IP address for '{domain_name}': {str(e)}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

def scan_ports(ip_address, ports):
    open_ports = []
    for port, service_name in ports.items():
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                s.connect((ip_address, port))
                open_ports.append((port, service_name))
        except ConnectionRefusedError:
            pass
        except TimeoutError:
            pass
        except Exception as e:
            print(f"Error scanning port {port}: {str(e)}")
    return open_ports

def main():
    common_ports = {
        21: "FTP",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        115: "SFTP",
        135: "RPC",
        139: "NetBIOS",
        143: "IMAP",
        194: "IRC",
        443: "SSL",
        445: "SMB",
        1433: "MSSQL",
        3306: "MySQL",
        3389: "Remote Desktop",
        5632: "PCAnywhere",
        5900: "VNC",
        25565: "Minecraft"
    }

    print("IP Address Resolver and Port Scanner")
    print("------------------------------------")
    
    while True:
        domain_name = input("Enter a domain name (or 'exit' to quit): ")
        if domain_name.lower() == 'exit':
            break
        
        ip_address = resolve_ip(domain_name)
        print("\nResolving IP address...")
        if not ip_address.startswith("Error"):
            print(f"IP Address: {ip_address}")
            
            open_ports = scan_ports(ip_address, common_ports)
            
            if open_ports:
                print("Open Ports:")
                for port, service_name in open_ports:
                    print(f"Port {port} ({service_name}) is open")
            else:
                print("No open ports found")
        else:
            print(ip_address)
        print("------------------------------------")

if __name__ == "__main__":
    main()
