 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import csv
#initializew our selem web driver
driver = webdriver.Chrome()

URL_leliye = "https://web.whatsapp.com"

driver.get(URL_leliye)

# wait for the user to scan the QR code

time.sleep(8)

with open("contacts.csv", newline='', encoding='utf-8') as csvfile:
    readContactsbhai = csv.reader(csvfile)

    for row in readContactsbhai:
        if len(row) != 2:
            print(f"Skipping invalid row: {row}")
            continue  # Skip rows that don't have exactly 2 columns

        phnNo, message = row  # Unpack phone number and message


        sameTab = (URL_leliye + "/send?phone=" + str(phnNo))

        driver.get(sameTab)

        time.sleep(49)

        content = driver.switch_to.active_element

        content.send_keys(message)

        #press the enterKey
        content.send_keys(Keys.RETURN)


        time.sleep(20)
