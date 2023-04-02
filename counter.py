def countEmail():
    # This first line is provided for you
    name = input("Enter file:")
    if len(name) < 1 : name = "mbox-short.txt"
    handle = open(name)
    emails = list()
    email_count = dict()
    for line in handle:
        if line.startswith('From'):
            line_split = line.split()
            if len(line_split) > 2:
                emails.append(line_split[1])
      
    for email in emails:
        email_count[email] = email_count.get(email, 0) + 1
    bignumber = None
    bigemail = None
    for Email,number in email_count.items():
        if bignumber is None or number > bignumber:
            bigemail = Email
            bignumber = number
    print(bigemail, bignumber)

   

## if you want to test locally run > python counter.py
if __name__ == "__main__":
    countEmail()
