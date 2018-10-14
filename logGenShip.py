from random import randint, choice
import requests


def log_generator():
        # Create a log line constructed of various variables
        mes_list = ["HTTP error 401 (UNAUTHORIZED)", "HTTP error 400 (bad request)", "HTTP error 403 (FORBIDDEN)",
                    "HTTP error 404 (not found)", "HTTP error 500 (internal server error)",
                    "SECURITY ALERT - Your host is under attack!"]

        quantity = [4231, 435, 256, 2456, 34567, 675, 5234, 3, 23, 5, 6234, 234, 325, 623456, 1, 4, 8, 5, 2345, 123, 76,
                    12345, 6534674586, 235423453, 231, 1221]

        host = ["host_1", "host_2", "host_3", "host_4", "host_5", "host_6", "host_7", "host_8", "host_9", "host_10",
                "host_11", "host_12", "host_13", "host_666"]

        ip_address = ["192.168.53.24", "10.10.12.138", "103.10.10.11", "192.168.1.1", "8.8.8.8", "4.4.4.4",
                      "192.168.32.123", "172.38.282.1"]

        rand_field = '"field_{0}":"same_value"' .format(randint(0, 9))

        log = '{{"message": "{message}", "type": "demo_logs", "host": "{host}", "quantity": {qty}, "IP_Address": ' \
              '"{ip_address}", {random_field}'.format(message=choice(mes_list), host=choice(host), qty=choice(quantity),
                                                      ip_address=choice(ip_address), random_field=rand_field)
        final_log = log + '}'
        
        host_url = accountUrl
        data = final_log
        r = requests.post(host_url, data)

        print(r.json)


x = int(input("How many log lines would you like? "))
accountUrl = input("Paste the url from log shipping page: ")
count = 0
while count in range(0, x):
        log_generator()
        count = count + 1
