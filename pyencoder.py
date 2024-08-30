import argparse
import urllib.parse
import base64
import sys

# Define encoding functions
def url_encode(payload):
    return ''.join(f'%{ord(c):02X}' for c in payload)

def partial_url_encode(payload):
    return payload.replace('(', '%28').replace(')', '%29').replace('<', '%3C').replace('>', '%3E')
def html_entity_encode(payload):
    return ''.join(f'&#{ord(c)};' for c in payload)

def hex_encode(payload):
    return ''.join(f'\\x{ord(c):02x}' for c in payload)

def base64_encode(payload):
    encoded = base64.b64encode(payload.encode()).decode()
    return f'<script>eval(atob("{encoded}"))</script>'

def double_url_encode(payload):
    return urllib.parse.quote(urllib.parse.quote(payload))

def hex_representation(payload):
    return ''.join(f'\\u{ord(c):04x}' for c in payload)

def octal_encode(payload):
    return ''.join(f'\\{oct(ord(c))[2:]}' for c in payload)

def javascript_escape(payload):
    return ''.join(f'\\x{ord(c):02x}' for c in payload)

def mixed_encoding(payload):
    return ''.join(f'&#x{ord(c):x};' for c in payload)

def inject_non_printable_chars(payload):
    return payload.replace('script', 'scri%00pt')

def fragment_script_tag(payload):
    return payload.replace('script', 'scr"+"ipt')

def use_backticks(payload):
    return payload.replace('1', '`1`')

def polyglot_payload(payload):
    return payload.replace('<script>', '<scri<script>pt>').replace('</script>', '</scri</script>pt>')

def inline_comments(payload):
    return payload.replace('script', 'scr<!-- -->ipt')

def alter_case(payload):
    return payload.lower().replace('script', 'sCriPt')

# List of encoding functions
encoding_functions = [
    url_encode,
    partial_url_encode,
    html_entity_encode,
    hex_encode,
    base64_encode,
    double_url_encode,
    hex_representation,
    octal_encode,
    javascript_escape,
    mixed_encoding,
    inject_non_printable_chars,
    fragment_script_tag,
    use_backticks,
    polyglot_payload,
    inline_comments,
    alter_case
]

def encode_payload(payload):
    encoded_payloads = []
    for func in encoding_functions:
        encoded_payloads.append(func(payload))
    return encoded_payloads

def encode_payloads_from_file(input_file, output_file=None):
    try:
        with open(input_file, 'r') as infile:
            payloads = infile.readlines()
            encoded_payloads = []
            for payload in payloads:
                payload = payload.strip()
                encoded_payloads.extend(encode_payload(payload))
            output_result(encoded_payloads, output_file)
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
        sys.exit(1)

def output_result(encoded_payloads, output_file=None):
    if output_file:
        try:
            with open(output_file, 'w') as outfile:
                for encoded in encoded_payloads:
                    outfile.write(f'{encoded}\n')
            print(f"Encoded payloads saved to '{output_file}'.")
        except IOError as e:
            print(f"Error: Unable to write to file '{output_file}': {e}")
            sys.exit(1)
    else:
        for encoded in encoded_payloads:
            print(encoded)

def main():
    print(banner)
    parser = argparse.ArgumentParser(
        description="Encode payloads with various techniques to bypass WAF or filters."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-p', '--payload', type=str, help='Single payload to encode.')
    group.add_argument('-l', '--list', type=str, help='File containing multiple payloads (one per line) to encode.')
    parser.add_argument('-o', '--output', type=str, help='Output file to save encoded payloads.')
    
    args = parser.parse_args()

    if args.payload:
        encoded_payloads = encode_payload(args.payload)
        output_result(encoded_payloads, args.output)
    elif args.list:
        encode_payloads_from_file(args.list, args.output)

banner = """
             __                 __        __   
            |__)  /\  \ / |    /  \  /\  |  \  
            |    /~~\  |  |___ \__/ /~~\ |__/                                     
             ___       __   __   __   ___  __  
            |__  |\ | /  ` /  \ |  \ |__  |__) 
            |___ | \| \__, \__/ |__/ |___ |  \ 

"Encode payloads with various techniques to bypass WAF or filters."
"""

if __name__ == '__main__':    
    main()
    
