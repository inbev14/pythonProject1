import re
filename = 'mbox.txt'
with open(filename) as f:
    text = f.read()
    pattern = r'[\w+]?[\.]?[\w+]?[\.]?\w+@\w+[\.]?[\w+]?[\.]?[\w+]?[\.]?[\w+]?'
    emails = re.findall(pattern, text)
    count_of_at = re.findall(r'@', text)
    # check = r'@.\w+'
    print(f'Found {len(emails)}, must be {len(count_of_at)}')
    # new_text = re.sub(pattern, "", text)
    print(emails)