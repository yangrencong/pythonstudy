loggers = []
if loggers:
    for logger in loggers:
        if logger == 'admin':
            print("Hello admin,would you like to see a status report?")
        else:
            print("Hello "+logger+",thank you for logging in again")
else:
    print("we need to find some users")
