# playwright-python-tests

![Tests](https://github.com/andres-simbana/playwright-python-tests/actions/workflows/tests.yml/badge.svg)

E2E test automation suite for [SauceDemo](https://www.saucedemo.com/) using **Playwright** and **Pytest**, following the **Page Object Model (POM)** pattern. Includes HTML report generation and CI/CD with GitHub Actions.

---

## 🛠️ Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=flat-square&logo=playwright&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=github-actions&logoColor=white)

---

## 📁 Project Structure

```
playwright-python-tests/
├── pages/
│   ├── login_page.py       # Login page interactions
│   ├── inventory_page.py   # Product listing page
│   └── cart_page.py        # Shopping cart page
├── tests/
│   ├── test_login.py
│   ├── test_inventory.py
│   └── test_cart.py
├── conftest.py             # Pytest fixtures (browser setup/teardown)
├── pytest.ini
└── requirements.txt
```

---

## ⚙️ Setup

### 1. Clone the repo
```bash
git clone https://github.com/andres-simbana/playwright-python-tests.git
cd playwright-python-tests
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Install Playwright browsers
```bash
playwright install
```

---

## ▶️ Running the tests

Run all tests:
```bash
pytest
```

Run a specific test file:
```bash
pytest tests/test_login.py
```

Run in headed mode (visible browser):
```bash
pytest --headed
```

Run in a specific browser:
```bash
pytest --browser firefox
pytest --browser webkit
```

---

## 📊 HTML Report

After running, the report is generated at:
```
reports/report.html
```

Open it in any browser to see detailed results.

---

## 🔄 CI/CD

Tests run automatically on every push via **GitHub Actions** (`.github/workflows/tests.yml`).
