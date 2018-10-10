# logGeneratorShipper

Very simple tool to generate demo logs and ship them to any environemt you want.
All you need is a terminal and the host ursl which you can get form the log shipping page.

1. To get the url, login to your account >> Log Shipping >> Libraries >> Bulk HTTP/S
2. Copy the relevant url (http or https)
3. Run the script using python3 and type the values you want:
  a. How many random log lines you want to ship
  b. The url you copied earlier (example: http://listener.logz.io:8070/?token=<your token>&type=MY-TYPE
     if you wish to change the type, just replace the "MY-TYPE" string
