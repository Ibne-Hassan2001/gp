# # This sample code supports Appium Python client >=2.3.0
# # pip install Appium-Python-Client
# # Then you can paste this into a file and simply run with Python
# from appium import webdriver
# import time
# from appium import webdriver
# from appium.options.common.base import AppiumOptions
# from appium.webdriver.common.appiumby import AppiumBy
#
# # For W3C actions
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.actions import interaction
# from selenium.webdriver.common.actions.action_builder import ActionBuilder
# from selenium.webdriver.common.actions.pointer_input import PointerInput
#
# options = AppiumOptions()
# options.load_capabilities({
# 	"platformName": "android",
# 	"appium:deviceName": "adb-f49dee58-rLknMB._adb-tls-connect._tcp",
# 	"appium:appPackage": "com.portonics.mygp",
# 	"appium:appActivity": "com.portonics.mygp.ui.MainActivity",
# 	"appium:ensureWebviewsHavePages": True,
# 	"appium:nativeWebScreenshot": True,
# 	"appium:newCommandTimeout": 3600,
# 	"appium:connectHardwareKeyboard": True
# })
# import csv
#
# # Connect to Appium server
# # Cdriver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)onnect to Appium server
#
# # Initialize driver object
#
# try:
#     # Connect to Appium server
#     driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)
#
#     # Add any additional actions you want to perform with your app here
#     # For example, click on an element with ID "btnGuest"
#     driver.find_element("id","com.portonics.mygp:id/btnGuest").click()
#
#     # Wait for a transition or any other operation to complete
#     time.sleep(1)  # Adjust the sleep time as needed
#     # Click on the offer button
#     offer_button = driver.find_element("xpath",
#                                        "(//android.widget.ImageView[@resource-id=\"com.portonics.mygp:id/ivIcon\"])[2]")
#     offer_button.click()
#     time.sleep(1)
#
#     rows = driver.find_element("id", "com.portonics.mygp:id/title")
#     scraped_data = []
#     count = 1
#
#     while True:
#             # element = driver.find_element("xpath", "//android.view.View[@bounds='[48,883][1296,1222]']")
#             # row = element.find_element("xpath", ".//android.widget.TextView[@resource-id='com.portonics.mygp:id/title']")
#             # Find the title element based on its resource ID and bounds attribute
#             row = driver.find_element("xpath", "//android.widget.TextView[@resource-id='com.portonics.mygp:id/title' and @bounds='[228,1306][1136,1360]']")
#             # Accessing an element using index and XPath
#             element = driver.find_element_by_xpath("(//android.view.View[@resource-id='com.portonics.mygp:id/cardView'])[1]")
#
#             print("Row Number", count)
#             count += 1
#             title = row.text
#             print(title)
#             # if not row:
#             #     break
#             # # xpath_pattern = "//android.widget.TextView[@resource-id=\'com.portonics.mygp:id/amount\' and contains(@text, '৳')]"
#             # # validity_element = row.find_element("xpath", "(//android.widget.TextView[@resource-id=\"com.portonics.mygp:id/validity\"])[1]")
#             # # validity = validity_element.text
#             # validity = driver.find_element("id", "com.portonics.mygp:id/validity").text
#             # amount = driver.find_element("id", "com.portonics.mygp:id/amount").text
#             # print(validity)
#             # amount = ""
#             #
#             # amount_element = driver.find_element("xpath", xpath_pattern)
#             # amount_text = amount_element.text
#             # amount = amount_text[1:]
#             # print("Amount Text:", amount)
#
#             scraped_data.append([title, validity, amount])
#     # Write the information to a CSV file
#     with open("offer_info.csv", "w", encoding="utf-8", newline="") as csvfile:
#         csv_writer = csv.writer(csvfile)
#         csv_writer.writerow(["Title", "Validity", "Amount"])
#         csv_writer.writerow([title, validity, amount])
#
#
#
#
# except Exception as e:
#     print("An error occurred:", e)
#
# finally:
#     # Quit the driver to release resources
#     if driver:
#         driver.quit()


# This sample code supports Appium Python client >=2.3.0
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput






options = AppiumOptions()
options.load_capabilities({
	"platformName": "android",
	"appium:deviceName": "OPPO A3s",
	"appium:ensureWebviewsHavePages": True,
	"appium:automationName": "UiAutomator2",
	"appium:platformVersion": "8.1.0",
	# "appium:undefined": undefined,
	"appium:nativeWebScreenshot": True,
	"appium:newCommandTimeout": 3600,
	"appium:connectHardwareKeyboard": True
})
import  csv
import time
driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(607, 578)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(142, 573)
actions.w3c_actions.pointer_action.release()
actions.perform()

time.sleep(2)

driver.find_element("xpath", "//android.widget.TextView[@text=\"My Robi\"]").click()
time.sleep(2)

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
locator = (AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='net.omobio.robisc:id/navViewDashboard']/android.widget.LinearLayout/android.widget.LinearLayout[4]")
# offer_button = driver.find_element("xpath", "(//android.widget.LinearLayout[@resource-id=\"net.omobio.robisc:id/linearLayout\"])[4]")
# offer_button = driver.find_element("xpath",
# 								   "(//androidx.recyclerview.widget.RecyclerView[@resource-id=\"net.omobio.robisc:id/recycler_view\"])[1]/android.view.ViewGroup[4]]")

# el = driver.find_element(by=AppiumBy.XPATH,value="(//android.widget.LinearLayout[@resource-id="net.omobio.robisc:id/linearLayout"])[4]")
# time.sleep(2)
offer_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locator))
offer_button.click()
time.sleep(2)

bundles = driver.find_element("xpath", "//android.widget.TextView[@resource-id=\"net.omobio.robisc:id/textView\" and @text=\"Bundles\"]")
bundles.click()
time.sleep(2)
# Wait for offers to load
# time.sleep(3)

# Find all FrameLayout elements
frame_layouts = driver.find_elements("xpath",	'//androidx.recyclerview.widget.RecyclerView[@resource-id="net.omobio.robisc:id/rvOffers"]/android.widget.FrameLayout')

# Prepare CSV file
csv_file = open('Bundle_offers.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['PackTitle', 'Validity', 'Price'])

first_elem="1"
session_end = False
pack_title="2"
from selenium.common.exceptions import NoSuchElementException
array=[]
for j in range(5):
	cnt = 0
	# Iterate through each FrameLayout
	if(session_end):
		break
	index=0

	frame_layout=frame_layouts[0]
	first_text =  frame_layout.find_element('id','net.omobio.robisc:id/tvPackPrice').text
	first_text=first_text[1:]
	print("frame_layouts[0]", first_text)
	print("first_elem]", first_elem)

	if(first_text==first_elem):
		break
	for i in range(len(frame_layouts)):
		frame_layout=frame_layouts[i]

		if (session_end):
			break
		if ((cnt==0) and(first_elem == pack_title)):
			session_end = True
			break
		try:
			# Extract PackTitle, Validity, and Price from the FrameLayout
			pack_title = frame_layout.find_element('id', 'net.omobio.robisc:id/tvPackTitle').text
			pack_title = pack_title[:len(pack_title) - 1]
			validity = frame_layout.find_element('id', 'net.omobio.robisc:id/tvValidity').text
			price = frame_layout.find_element('id', 'net.omobio.robisc:id/tvPackPrice').text
			price = price[1:]

			# Write the data to the CSV file
			if(pack_title  not in array):
				csv_writer.writerow([pack_title, validity, price])
				array.append(pack_title)
			# Print the extracted data
			print(f"Offer {index}:")
			print(f"Pack Title: {pack_title}")
			print(f"Validity: {validity}")
			print(f"Price: {price}")
			print()
		except NoSuchElementException:
			# Handle NoSuchElementException by printing a message and continuing to the next iteration
			print(f"No such element found for Offer {index}")
			continue

		# Extract PackTitle, Validity, and Price from the FrameLayout
		# pack_title = frame_layout.find_element('id','net.omobio.robisc:id/tvPackTitle').text
		# pack_title=pack_title[:len(pack_title)-1]
		# validity = frame_layout.find_element('id','net.omobio.robisc:id/tvValidity').text
		# price = frame_layout.find_element('id','net.omobio.robisc:id/tvPackPrice').text
		# price = price[1:]

		if (cnt == 0):
			if (first_elem == pack_title):
				session_end = True
				break
			first_elem = price
			print("first_elem", first_elem)
			print("pack_title", pack_title)
		# Write the data to the CSV file
		# csv_writer.writerow([pack_title, validity, price])

		# # Print the extracted data
		# print(f"Offer {index}:")
		# print(f"Pack Title: {pack_title}")
		# print(f"Validity: {validity}")
		# print(f"Price: {price}")
		# print()
		cnt+=1
		index+=1

	print("iteration",j)
	actions = ActionChains(driver)
	actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
	actions.w3c_actions.pointer_action.move_to_location(357, 1279)
	actions.w3c_actions.pointer_action.pointer_down()
	actions.w3c_actions.pointer_action.move_to_location(360, 779)
	actions.w3c_actions.pointer_action.release()
	actions.perform()

	frame_layouts = driver.find_elements("xpath",
										 '//androidx.recyclerview.widget.RecyclerView[@resource-id="net.omobio.robisc:id/rvOffers"]/android.widget.FrameLayout')



# Close the CSV file
csv_file.close()