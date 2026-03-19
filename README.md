# playwright-python-tests

Modern browser E2E automation framework built with **Playwright** and **pytest**, following the **Page Object Model (POM)** design pattern.

## Stack

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python)
![Playwright](https://img.shields.io/badge/Playwright-1.x-green?style=flat-square&logo=playwright)
![Pytest](https://img.shields.io/badge/Pytest-8.x-blue?style=flat-square&logo=pytest)
![CI](https://github.com/Anseb77/playwright-python-tests/actions/workflows/tests.yml/badge.svg)

## Project Structure

```
playwright-python-tests/
├── .github/workflows/     # CI/CD with GitHub Actions
├── pages/                 # Page Object Model classes
│   ├── login_page.py
│   └── inventory_page.py
├── tests/
│   ├── test_login.py
│   └── test_inventory.py
├── conftest.py            # Shared fixtures and hooks
├── requirements.txt
└── pytest.ini
```

## Test Coverage

| Module    | Test Cases                                                      |
|-----------|-----------------------------------------------------------------|
| Login     | Valid login, invalid credentials, empty fields, locked user     |
| Inventory | Items count, add to cart, multiple items, cart navigation       |

## Setup

```bash
pip install -r requirements.txt
playwright install chromium
pytest
```

Reports are generated in `reports/report.html`.

## CI

Tests run automatically on every push and pull request via GitHub Actions.
