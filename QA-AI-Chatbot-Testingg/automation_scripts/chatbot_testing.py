from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Set up the driver
driver = webdriver.Chrome()

# Open chatbot webpage
driver.get("https://your-chatbot-url.com")

# Define test cases
test_cases = [
    ("Hi", ["Hello", "Hi! How can I assist?"]),
    ("What is 2+2?", ["4"]),
    ("Tell me a joke", ["Why did", "joke"]),
    ("Goodbye", ["See you soon!", "Goodbye!"]),
    ("Random text", ["I don’t understand"]),
    ("What’s your name?", ["I am an AI chatbot!"]),
    ("😊😂🤔", ["I can’t process emojis"]),
    ("SELECT * FROM users;", ["Invalid input"]),
    ("Hola", ["Sorry, I only understand English."]),
]

# Run tests
for user_input, expected_responses in test_cases:
    try:
        chatbox = driver.find_element("id", "chatbox")
        chatbox.send_keys(user_input)
        chatbox.send_keys(Keys.RETURN)
        time.sleep(2)  # Wait for response

        response = driver.find_element("id", "response").text
        assert any(resp in response for resp in expected_responses), f"❌ Test Failed: {user_input} | Got: {response}"
        print(f"✅ Test Passed: {user_input} | Response: {response}")

    except Exception as e:
        print(f"⚠️ Error while testing '{user_input}': {str(e)}")

print("🚀 All tests completed!")
driver.quit()
