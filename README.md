# Pytest End-to-End automations

A [Python-based end-to-end (E2E) test automation framework](https://supriya-mainalli.github.io/pytest-automations-e2e/#install) built with **Pytest**, **Selenium WebDriver**, and **Allure** reporting. This for learning and experimentation with API and webautomations. The project follows the **Page Object Model (POM)** design pattern and currently covers web UI automation for the [OrangeHRM demo application](https://opensource-demo.orangehrmlive.com/).

---

## 📁 Project Structure

```
pytest-automations-e2e/
├── API/
│   └── __init__.py              # Placeholder for future API test modules
│
├── WebAutomations/
│   ├── __init__.py
│   ├── config.ini               # Browser and URL configuration
│   ├── conftest.py              # Pytest fixtures and hooks (setup/teardown, screenshots)
│   │
│   ├── locators/
│   │   ├── __init__.py
│   │   └── login_page.py        # Selenium locators for Login page elements
│   │
│   ├── pages/
│   │   ├── __init__.py
│   │   └── login_page.py        # Page Object for Login page actions
│   │
│   └── tests/
│       ├── __init__.py
│       └── test_login.py        # Test cases for Login functionality
│
└── config.py                    # Utility to read config.ini values
```

---

## ✅ Features

- **Page Object Model (POM)** — Clean separation of locators, page actions, and test logic.
- **Allure Reporting** — Rich HTML reports with test steps, severity levels, and failure screenshots.
- **Auto Screenshot on Failure** — Captures browser screenshot and attaches it to the Allure report when a test fails.
- **Configurable via `config.ini`** — Browser type and target URL are externalized for easy environment switching.
- **Pytest Markers** — Tests are tagged with `smoke` and custom IDs (e.g., `testId001`) for selective test execution.
- **Extensible API Module** — An `API/` package is scaffolded and ready for REST API test cases.

---

## 🛠️ Prerequisites

- Python 3.8+
- Google Chrome browser
- ChromeDriver (matching your Chrome version) available on `PATH`

---

## ⚙️ Installation

```bash
# 1. Clone the repository
git clone https://github.com/supriya-mainalli/pytest-automations-e2e.git
cd pytest-automations-e2e

# 2. Create and activate a virtual environment (recommended)
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install pytest selenium allure-pytest
```

---

## 🔧 Configuration

Edit `WebAutomations/config.ini` to change the browser or target URL:

```ini
[basic info]
browser=chrome
endpoint=https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
```

> **Note:** The `config.py` root file reads from `config.ini` using a relative path. Run pytest from the project root to ensure the path resolves correctly.

---

## ▶️ Running Tests

```bash
# Run all tests
pytest WebAutomations/tests/

# Run only smoke tests
pytest WebAutomations/tests/ -m smoke

# Run with verbose output
pytest WebAutomations/tests/ -v

# Run and generate Allure results
pytest WebAutomations/tests/ --alluredir=allure-results

# Serve the Allure report (requires Allure CLI installed)
allure serve allure-results
```

---

## 📊 Allure Report

Each test is annotated with:
- `@allure.feature` — High-level feature group
- `@allure.story` — User story / scenario
- `@allure.severity` — Severity level (`CRITICAL`, `NORMAL`, etc.)
- `allure.step` — Step-by-step breakdown in the report

On test failure, a **PNG screenshot** is automatically captured and attached to the report for easy debugging.

---

## 🧪 Test Cases

| Test ID    | Marker | Description            | Severity |
|------------|--------|------------------------|----------|
| testId001  | smoke  | Valid Login to OrangeHRM | CRITICAL |

---

## 🤝 Contributing

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request.

---
