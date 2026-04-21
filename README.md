# NopCommerce Demo – Selenium Python Automation Framework

## Project Overview
End-to-end test automation framework for [demo.nopcommerce.com](https://demo.nopcommerce.com/), a popular e-commerce demo site. Designed to demonstrate **enterprise-grade testing practices** including Page Object Model (POM), Data-Driven Testing (DDT), and cross-browser execution.

**Why this matters:**  
This framework mirrors the testing approach needed for public/enterprise systems — data integrity, login security, customer data management, and search/retrieval accuracy.

---

## Tech Stack
| Category | Tools |
|----------|-------|
| Language | Python 3.x |
| Automation | Selenium WebDriver |
| Test Runner | Pytest |
| Framework | Page Object Model (POM) |
| Data-Driven | DDT (JSON/Excel) |
| Reporting | Pytest-HTML |
| Logging | Custom logger (utilities) |
| Parallel Execution | pytest-xdist (ready) |

---

## Folder Structure
demo-NopCommerceApp/
├── pageObjects/ # Locators + methods per page
├── testCases/ # All test scripts
│ ├── conftest.py # Pytest fixtures (setup/teardown)
│ ├── pytest.ini # Pytest configuration
│ ├── test_loginPage.py # Basic login validation
│ ├── test_loginPage_ddt.py # Data-driven login tests
│ ├── test_add_newCustomer.py # Customer creation flow
│ └── test_search_customers.py # Customer search validation
├── utilities/ # Custom wrappers, Excel readers, logging
├── Configurations/ # Config files (URLs, credentials)
├── TestData/ # Test data (JSON/Excel/CSV)
├── Logs/ # Execution logs
├── Reports/ # HTML test reports
├── ScreenShots/ # Screenshots on test failure
├── requirements # Dependencies list
└── run.bat # One-click execution

---

## Test Coverage (Matches Your Test Cases)

| Test File | What It Validates |
|-----------|-------------------|
| `test_loginPage.py` | Valid/invalid login, error messages, session management |
| `test_loginPage_ddt.py` | Data-driven login (multiple users from JSON/Excel) |
| `test_add_newCustomer.py` | Add new customer — form validation, data persistence |
| `test_search_customers.py` | Search customers by name/email — results accuracy |

---

## How to Run Tests

**Step 1. Clone the repository**
git clone https://github.com/click2jay1/demo-NopCommerceApp.git
cd demo-NopCommerceApp

**Step 2. Create virtual environment (recommended)**
python -m venv .venv
.venv\Scripts\activate   # On Windows
source .venv/bin/activate  # On Mac/Linux

**Step 3: Install dependencies**
pip install -r requirements

**Step 4: Run all tests**
pytest testCases/ -v --html=Reports/report.html

**Step 5: Run a single test file**
pytest testCases/test_loginPage_ddt.py -v

**Alternative: One-click execution**
Double-click run.bat

## Key Features
- Page Object Model for maintainability
- Data-Driven Testing with external files
- Screenshots on test failure
- HTML reports for stakeholders
- Config separation (no hardcoded data)

## Why This Framework Matters for Staff/Senior Quality Assurance Engineer Role
- Demonstrates automation-first mindset
- Shows scalable, maintainable framework design
- Includes data integrity validation (customers, login)
- Ready for CI/CD integration

# Author
Jay Raj Prakash
ISTQB Advanced Level (CTAL-TAE) Certified
📧 jayrajprakash@outlook.com
🔗 [GitHub Profile](https://github.com/click2jay1)
📍 Greater Seattle Area, WA
