# EdTech Automation Testing Project

## Project Overview

This project automates the testing of the GUVI EdTech website using Selenium WebDriver with Python and the Page Object Model (POM) design pattern. The project verifies important functionalities such as homepage navigation, login, logout, signup redirection, menu validation, and chatbot visibility.

---

## Technologies Used

- Python 3.14
- Selenium WebDriver
- Pytest
- Pytest HTML
- ChromeDriver
- Page Object Model (POM)
- python-dotenv

---

## Project Structure

```
Edtech Project/
│
├── pages/
│   ├── __init__.py
│   ├── home_page.py
│   ├── login_page.py
│   └── menu_page.py
│
├── tests/
│   ├── __init__.py
│   ├── test_home_page.py
│   ├── test_login_page.py
│   └── test_menu_page.py
│
├── reports/
│   └── report.html
│
├── .env.example
├── .gitignore
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Test Cases Covered

### Home Page

- Verify homepage URL
- Verify homepage title
- Verify Login button
- Verify Sign Up button visibility and clickability
- Verify Sign Up page redirection

### Login Page

- Verify login with valid credentials
- Verify login with invalid credentials
- Verify logout functionality

### Menu Page

- Verify Courses, LIVE Classes and Practice menu items
- Verify chatbot widget visibility

Total Test Cases: **10**

---

## Installation

Clone the repository.

```bash
git clone <repository-url>
```

Move into the project directory.

```bash
cd Edtech-Project
```

Install the required packages.

```bash
py -m pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

Example:

```text
GUVI_EMAIL=your_email
GUVI_PASSWORD=your_password
```

**Do not upload your actual `.env` file to GitHub.**

---

## Running the Tests

Run all test cases.

```bash
py -m pytest
```

Generate the HTML report.

```bash
py -m pytest --html=reports/report.html --self-contained-html
```

---

## Test Report

The HTML report is generated inside the `reports` folder.

```
reports/report.html
```

---

## Framework Features

- Page Object Model (POM)
- Explicit Waits
- Reusable Methods
- Secure Credentials using `.env`
- HTML Test Reports
- Easy to Maintain
- Modular Project Structure

---

## Author

Gayatri N
