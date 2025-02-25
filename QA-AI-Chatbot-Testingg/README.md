# QA AI Chatbot Testing

## 📌 About This Project
This project is designed to **test an AI-based chatbot** using **manual test cases** and **automation scripts**. It includes:
- Well-defined **test cases** for chatbot responses
- **Automation testing** using Selenium
- A structured **test plan** and bug reports

---

## 📂 Project Contents
- `chatbot_test_cases.txt` → Contains test cases for the chatbot
- `test_plan.md` → Detailed testing strategy & scenarios
- `bug_report.md` → Documented issues and findings
- `automation_scripts/` → Python scripts for automated chatbot & API testing

---

## 🚀 How to Run the Automation Script
1. Install **Python** and required libraries:
```bash
pip install selenium
```

2. Run the chatbot test script:
```bash
python automation_scripts/chatbot_testing.py
```

---

## 📊 Sample Test Outputs

| Test Case | Input | Expected Output | Actual Output | Status |
|-----------|-------|----------------|---------------|--------|
| TC-001 | Hi | "Hello! How can I assist?" | "Hello! How can I assist?" | ✅ Pass |
| TC-002 | What is 2+2? | "4" | "4" | ✅ Pass |
| TC-003 | Tell me a joke | A joke response | "Why did the chicken cross the road?" | ✅ Pass |
| TC-010 | What’s the weather? | Weather-related response | "Currently, it's sunny." | ✅ Pass |
| TC-011 | SELECT * FROM users; | No security vulnerability | "Invalid input detected." | ✅ Pass |

---

## 🛠 Future Enhancements
- API integration testing
- Performance testing for chatbot response time
- Testing chatbot adaptability with diverse user inputs

---

## 📬 Contact
If you have suggestions or find bugs, feel free to open an issue!
