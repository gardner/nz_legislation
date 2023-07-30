import re

def clean(data):
    cleaned = []

    data = re.sub(r'\r\n', '\n', data)
    data = re.sub(r'\n\r', '\n', data)
    data = re.sub(r'\n\n', '\n', data)

    for line in data.split('\n'):
        while '  ' in line:
            line = line.replace('  ', ' ')
        if line.startswith(' '):
            line = line[1:]
        while '\r\n' in line:
            line = line.replace('\r\n', '\n')
        while '\n\n' in line:
            line = line.replace('\n\n', '\n')
        # while re.match(r'\n ', line):
        #     line = line.replace('\n ', '\n')
        # while re.match(r' \n', line):
        #     line = line.replace(' \n', '\n')

        if line != '':
            cleaned.append(line.strip())

    return "\n".join(cleaned)

