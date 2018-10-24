# import packages
import time
from datetime import datetime



# hosts setup
#hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
hosts_path=r"D:\dev\practice_workspace\app3_webblocker\resources\hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com","www.reddit.com","reddit.com"]

# infinite loop
while True :
    if 8 <= datetime.now().hour < 16 :      # block websites
        print("Working hours...")
        with open(hosts_path,'r+') as f :
            content=f.read()
            for website in website_list :
                if website in content :
                    pass
                else :
                    f.write(redirect+"\t\t\t"+website+"\n")
    else :                  # don't block websites
        with open(hosts_path,'r+') as f :
            content=f.readlines()
            f.seek(0)
            for line in content :
                if not any(website in line for website in website_list) :
                    f.write(line)
            f.truncate()
        print("Outside working hours...")



    time.sleep(5)
