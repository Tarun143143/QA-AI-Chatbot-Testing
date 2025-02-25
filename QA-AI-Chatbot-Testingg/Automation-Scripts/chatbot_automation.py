from selenium import webdriver

# Initialize WebDriver
driver = webdriver.Chrome()

# Open Chatbot Page (Replace with actual URL)
driver.get("https://example.com/chatbot")

# Locate input box and send message
input_box = driver.find_element("name", "chat_input")
input_box.send_keys("Hello")

# Submit the message
input_box.submit()

# Close browser
driver.quit()
