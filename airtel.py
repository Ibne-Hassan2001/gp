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

driver.find_element("xpath", "//android.widget.TextView[@text=\"My Airtel\"]").click()

time.sleep(2)

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
locator = (AppiumBy.XPATH, "//android.widget.LinearLayout[@resource-id=\"net.omobio.airtelsc:id/tabOffers\"]")
# # offer_button = driver.find_element("xpath", "(//android.widget.LinearLayout[@resource-id=\"net.omobio.robisc:id/linearLayout\"])[4]")
# # offer_button = driver.find_element("xpath",
# # 								   "(//androidx.recyclerview.widget.RecyclerView[@resource-id=\"net.omobio.robisc:id/recycler_view\"])[1]/android.view.ViewGroup[4]]")
#
# # el = driver.find_element(by=AppiumBy.XPATH,value="(//android.widget.LinearLayout[@resource-id="net.omobio.robisc:id/linearLayout"])[4]")
# # time.sleep(2)
offer_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locator))

# offer_button =  driver.find_element("xpath", "//android.widget.LinearLayout[@resource-id=\"net.omobio.airtelsc:id/tabOffers\"]")
offer_button.click()
time.sleep(2)
driver.find_element("xpath",	'//android.widget.TextView[@resource-id="net.omobio.airtelsc:id/textView" and @text="7 Days"]').click()


# bundles = driver.find_element("xpath", "//android.widget.TextView[@resource-id=\"net.omobio.robisc:id/textView\" and @text=\"Bundles\"]")
# bundles.click()
# time.sleep(2)
# # Wait for offers to load
# # time.sleep(3)
#
# Find all FrameLayout elements

# Prepare CSV file
csv_file = open('Internet_offers_airtel.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['PackTitle', 'Validity', 'Price'])


def run(driver):
	frame_layouts = driver.find_elements("xpath",
										 '//androidx.recyclerview.widget.RecyclerView[@resource-id="net.omobio.airtelsc:id/rvOffers"]/android.widget.FrameLayout')



	first_elem = "1"
	session_end = False
	pack_title = "2"
	from selenium.common.exceptions import NoSuchElementException
	array = []
	for j in range(2):
		cnt = 0
		# Iterate through each FrameLayout
		if(session_end):
			print("session end")
			break
		index=0

		frame_layout=frame_layouts[0]

		first_text =  frame_layout.find_element('id','net.omobio.airtelsc:id/tvPackPrice').text
		if(first_text[len(first_text)-1]!='B' and first_text[len(first_text)-1]!='s'):
			first_text = first_text[:len(first_text) - 1]
		if not first_text[0].isdigit():
			first_text=first_text[1:]
		print("frame_layouts[0]", first_text)
		print("first_elem]", first_elem)

		if(first_text==first_elem):
			print("first_text==first_elem")
			break
		for i in range(len(frame_layouts)):
			frame_layout=frame_layouts[i]

			if (session_end):
				print("session end")
				break
			if ((cnt==0) and(first_elem == pack_title)):
				session_end = True
				break
			try:
				# Extract PackTitle, Validity, and Price from the FrameLayout
				pack_title = frame_layout.find_element('id', 'net.omobio.airtelsc:id/tvPackTitle').text
				if (pack_title[len(pack_title) - 1] != 'B' and pack_title[len(pack_title) - 1] != 's' and  pack_title[len(pack_title) - 1] != 'e' and pack_title[len(pack_title) - 1] != '.' and pack_title[len(pack_title) - 1] != 'l'  ):
					pack_title = pack_title[:len(pack_title) - 1]
				if not pack_title[0].isdigit():
					pack_title = pack_title[1:]
				if(pack_title[len(pack_title) - 1] == '.'):
					pack_title=pack_title[:len(pack_title) - 3]
					pack_title+='kTok'
				validity = frame_layout.find_element('id', 'net.omobio.airtelsc:id/tvValidity').text
				price = frame_layout.find_element('id', 'net.omobio.airtelsc:id/tvPackPrice').text
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
		actions.w3c_actions.pointer_action.move_to_location(357, 1186)
		actions.w3c_actions.pointer_action.pointer_down()
		time.sleep(1)
		actions.w3c_actions.pointer_action.move_to_location(360, 796)
		actions.w3c_actions.pointer_action.release()
		actions.perform()

		frame_layouts = driver.find_elements("xpath",	'//androidx.recyclerview.widget.RecyclerView[@resource-id="net.omobio.airtelsc:id/rvOffers"]/android.widget.FrameLayout')

run(driver)
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(366, 523)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(366, 1125)
actions.w3c_actions.pointer_action.release()
actions.perform()


driver.find_element("xpath",	'//android.widget.TextView[@resource-id="net.omobio.airtelsc:id/textView" and @text="30 Days"]').click()

run(driver)

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(366, 523)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(366, 1125)
actions.w3c_actions.pointer_action.release()
actions.perform()


actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(668, 384)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(357, 381)
actions.w3c_actions.pointer_action.release()
actions.perform()

driver.find_element("xpath",	'//android.widget.TextView[@resource-id="net.omobio.airtelsc:id/textView" and @text="Unlimited"]').click()
run(driver)
csv_file.close()
driver.press_keycode(3)
# Close the CSV file
