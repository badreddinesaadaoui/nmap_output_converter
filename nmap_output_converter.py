import xml.etree.ElementTree as ET
import json
import sys

def color_text(text, color):
    colors = {
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'reset': '\033[0m',
    }
    return f"{colors[color]}{text}{colors['reset']}"

def xml_to_greppable(xml_file, output_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    with open(output_file, 'w') as f:
        for host in root.iter('host'):
            address = host.find('address').get('addr')
            status = host.find('status').get('state')

            for port in host.iter('port'):
                port_num = port.get('portid')
                protocol = port.get('protocol')

                state = port.find('state').get('state')
                name = port.find('service').get('name')

                if state == "open":
                    color = 'green'
                else:
                    color = 'red'

                result = f"{address}:{port_num}/{protocol} ({state}) {name}"
                f.write(color_text(result, color) + '\n')
                print(color_text(result, color))

def xml_to_json(xml_file, output_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    data = {}
    for host in root.iter('host'):
        address = host.find('address').get('addr')
        status = host.find('status').get('state')
        ports = []

        for port in host.iter('port'):
            port_num = port.get('portid')
            protocol = port.get('protocol')
            state = port.find('state').get('state')
            name = port.find('service').get('name')
            ports.append({
                "port_num": port_num,
                "protocol": protocol,
                "state": state,
                "name": name
            })

        data[address] = {
            "status": status,
            "ports": ports
        }

    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)

def xml_to_script_kiddie(xml_file, output_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    with open(output_file, 'w') as f:
        for host in root.iter('host'):
            address = host.find('address').get('addr')
            status = host.find('status').get('state')
            ports = []

            for port in host.iter('port'):
                port_num = port.get('portid')
                protocol = port.get('protocol')
                state = port.find('state').get('state')
                name = port.find('service').get('name')
                f.write(f"{address}:{port_num} ({protocol}) ({state}) ({name})\n")

    if name == "main":
        if len(sys.argv) != 4:
            print("Usage: python script.py [xml file] [output file] [format]")
            print("Format can be either 'greppable', 'json' or 'script_kiddie'")
            sys.exit(1)
xml_file = sys.argv[1]
output_file = sys.argv[2]
format = sys.argv[3]

if format == "greppable":
    xml_to_greppable(xml_file, output_file)
elif format == "json":
    xml_to_json(xml_file, output_file)
elif format == "script_kiddie":
    xml_to_script_kiddie(xml_file, output_file)
else:
    print(f"Invalid format: {format}")
    sys.exit(1)
