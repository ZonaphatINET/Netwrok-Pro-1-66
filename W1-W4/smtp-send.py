import smtplib

message = """From: From Person <...>
To: To Person <...>
...
"""

try:
    smtpObj = smtplib.SMTP('192.168.15.129')
    smtpObj.sendmail("inet@inet-virtual-machine", "inet@inet-virtual-machine", message)
    print("Successfully sent email")
except Exception as err:
    print(str(err))
