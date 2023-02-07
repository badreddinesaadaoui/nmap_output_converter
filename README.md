XML to Various Formats Converter

This python script converts an XML file to either a greppable, JSON, or a "script kiddie" format. The script uses the `xml.etree.ElementTree` module to parse the XML file, and the `json` module to convert to JSON format.

Usage :

To use this script, run the following command in your terminal:

    python script.py [xml file] [output file] [format]

The script takes in 3 arguments :

    1- `xml file` - the input xml file to be parsed
    2- `output file` - the file to output the results
    3- `format` - the format of the output, which can be either `greppable`, `json`, or `script_kiddie`.

Output Formats :

    1- `greppable` - the output is formatted in a way that is easier to be grepped, with each line indicating the address, port, protocol, state, and name of a service. The output is also colored based on the state of the service (green for open, red for closed).
    2- `json` - the output is formatted in JSON format, with each address as the key and its information (status, ports) as its value.
    3- `script_kiddie` - the output is a simple list of the address, port, protocol, state, and name of each service.
    
Example : 

    python script.py scan_results.xml output.txt greppable

This command will convert the `scan_results.xml` file to greppable format and write the output to `output.txt`.
