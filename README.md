# WhatsApp Automation

This project automates the process of sending messages on WhatsApp using **Selenium WebDriver**. The functionality is designed to read contact numbers and corresponding messages from a CSV file and send messages to each contact with a delay of 8-10 seconds between messages.

---

## 🚀 Features

- Automates sending WhatsApp messages.
- Reads contacts and messages from a CSV file.
- Includes a configurable delay between messages.
- Uses Selenium WebDriver to interact with the WhatsApp Web interface.

---

## 🛠️ Technologies Used

- **Python**: Programming language for the script.
- **Selenium**: WebDriver for automating browser interactions.
- **CSV**: File format for storing contact numbers and messages.

---

## 📁 Project Structure

```
whatsapp-automation/
├── main.py                 # Main automation script
├── contacts.csv            # CSV file with contacts and messages
├── README.md               # Project documentation
└── requirements.txt        # Dependencies
```

---

## ⚙️ Prerequisites

1. Install Python (v3.7+ recommended).
2. Install Google Chrome and download the [ChromeDriver](https://chromedriver.chromium.org/).
3. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   Example requirements:
   ```
   selenium
   ```

---

## 📂 CSV File Format

The `contacts.csv` file should have the following format:

| Contact Number | Message         |
|----------------|-----------------|
| 1234567890     | Hello, Priyanshu!    |
| 9876543210     | How are you?    |

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Automation-WA.git
   cd Automation-WA
   ```

2. Launch the script:
   ```bash
   python main.py
   ```

3. Scan the QR code on the WhatsApp Web page to log in.

4. The script will automatically send messages to the contacts listed in the `contacts.csv` file.

---

## 📋 Code Overview

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv

# Initialize the Selenium WebDriver
driver = webdriver.Chrome()




## 🛡️ Notes and Considerations

- **QR Code Scanning**: You must manually scan the QR code when running the script.
- **Delays**: The script includes delays (8-10 seconds) to avoid being flagged as spam.
- **Privacy**: Ensure you comply with WhatsApp's terms of service and privacy policies when using this automation.

---

## 💡 Future Enhancements

- Add a GUI for user-friendly input of contacts and messages.
- Support for group messaging.
- Implement error handling for invalid contacts or messages.

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

---

## 📝 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## 📧 Contact

For questions or feedback, please reach out to [Your Email Address].  

Happy automating! 🎉
