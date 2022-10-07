import re
from prettytable import PrettyTable


def read_file(file: str):
    """read file and return list with emails"""
    with open(file) as f:
        text = f.read()
        pattern = r'[\w*\.*]*@[\w*\.]*'
        return re.findall(pattern, text)
    
    
def make_dictionary_with_emails(full_emails: list):
    """enter emails and return normalized dictionary with emails"""
    dict_emails = {}
    for email in full_emails:
        key = email.split('@')[1]
        dict_emails.setdefault(key, [])
        if not email in dict_emails[key]:
            dict_emails[key].append(email)
    return dict_emails
    
    
def main():
    list_emails = read_file(filename)
    dict_emails = make_dictionary_with_emails(list_emails)
    email_table = PrettyTable()
    email_table.field_names = ['domain', 'number of emails']
    for domain, email in dict_emails.items():
        email_table.add_row([domain, len(email)])
    return email_table


if __name__ == '__main__':
    filename = 'mbox.txt'
    print(main())
    
    
    