import pyautogui as gui
import time

possible = []
combinations = []

# Define the positons of the items ie button and field input
fied_x, field_y, button_y, button_x = 0

for i in range(10):
    for j in range(10):
        for k in range(10):
            combinations.append(f"8{i}{j}{k}9")

def write_to_notepad():
    with open('combinations.txt', 'w') as file:
        for combo in combinations:
            file.write(f"{combo}\n")

# Get position of current mouse Location. Use this to get the locastion of 
# A --> The Field Coordinates
# B --> The Button Coordinates
def get_pos():
    for i in range (3):
        pos = gui.position()
        print(pos)
        time.sleep(1)



# Move to the field to enter the value
def move_to_field(button_x, button_y):
    gui.moveTo(141, 330, 1)
    time.sleep(1)
    gui.doubleClick()
    i = 0
    # Writes to the combinations text file all the possible combinations
    with open('combinations.txt', 'r') as file:
        for i, line in enumerate(file):
            gui.doubleClick()
            tracking_number = line.strip()
            
            # Move to the button
            gui.moveTo(button_x, button_y)
            gui.doubleClick()

            
            print(tracking_number)
            
            gui.typewrite(tracking_number)
          
            gui.moveTo(377, 361, 1)
         
            gui.click()
            time.sleep(5)
         
            
            if (gui.locateOnScreen('icon.png', confidence=0.6, grayscale=True)):
                gui.moveTo(999, 120, 1)
                print(f"Tracking number at line {i + 1} not existent, {tracking_number}")
            else:
                possible.append(tracking_number)
                print(f"Possible match #: {tracking_number} at line {i + 1}")
                gui.moveTo(0, 0, 1)
move_to_field(fied_x, field_y, button_y, button_x )




# import cfscrape
# url = "https://www.dhl.com/utapi?trackingNumber=8725896200&language=en&requesterCountryCode=NA&source=tt"
# scrape = cfscrape.create_scraper()

# res = scrape.get(url)
# print(res.status_code)

# import cloudscraper

# request_url = "https://www.dhl.com/utapi?trackingNumber=8725896200&language=en&requesterCountryCode=NA&source=tt"
# scraper = cloudscraper.create_scraper()
# res = scraper.get(request_url)

# print(res.status_code)




# import requests

# request_url = "https://www.dhl.com/utapi?trackingNumber=8725896200&language=en&requesterCountryCode=NA&source=tt"

# tracking_number = 8725896200
# payload = {
#     "trackingNumber": tracking_number,
#     "language": "en",
#     "requesterCountryCode": "NA",
#     "source" : "tt"
# }

# r = requests.post(request_url, data= payload )

# print(r.text)
# print(r.status_code)