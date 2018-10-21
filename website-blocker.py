import time
from datetime import datetime as dt

# if the path starts with a file name beginning with "n" then you write hosts_path = r"\filepath". r is for raw. This file path is for mac.
hosts_temp = "hosts1"
hosts_path = "/private/etc/hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com","facebook.com","youtube.com","www.youtube.com"]

while True:
    if (dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() <dt(dt.now().year,dt.now().month,dt.now().day,12)):
        print("working hours..")
        with open(hosts_path,"r+") as host_file:
            # will read the whole file at once
            content = host_file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    host_file.write(redirect + " " + website + "\n")

    else:
        with open(hosts_path,"r+") as host_file:
            # will read one line at a time
            content = host_file.readlines()
            # pointer will be at the beginning of the file
            host_file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    host_file.write(line)
            # truncates the file
            host_file.truncate()
            print("Fun hours..")
    time.sleep(5)

# to add this python script to your activity monitor
# 1. open terminal
# 2. sudo crontab -e
# 3. add at the end -> @reboot python file-path-to-website-blocker.py
