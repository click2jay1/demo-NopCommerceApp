# NopCommerce Demo – Selenium Python Automation Framework

## Project Overview
End-to-end test automation framework for demo.nopcommerce.com, a widely used e-commerce demo platform. This project demonstrates enterprise-grade QA practices, including Page Object Model (POM), Data-Driven Testing (DDT), and cross-browser execution.

**Why this matters:**  
The framework reflects real-world testing needs for enterprise and financial systems, ensuring data integrity, authentication reliability, customer data management, and search accuracy.

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

```text
demo-NopCommerceApp/
├── pageObjects/        # Page classes (locators + methods)
├── testCases/          # Test scripts
│   ├── conftest.py     # Fixtures (setup/teardown)
│   ├── pytest.ini      # Pytest configuration
│   ├── test_loginPage.py
│   ├── test_loginPage_ddt.py
│   ├── test_add_newCustomer.py
│   └── test_search_customers.py
├── utilities/          # Helpers (Excel, logging, reusable functions)
├── Configurations/     # Environment configs (URLs, credentials)
├── TestData/           # JSON / Excel / CSV test data
├── Logs/               # Execution logs
├── Reports/            # HTML reports
├── ScreenShots/        # Failure screenshots
├── requirements.txt    # Dependencies
└── run.bat             # One-click execution (Windows)
```
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

### Step 1: Clone the repository
```text
git clone https://github.com/click2jay1/demo-NopCommerceApp.git
cd demo-NopCommerceApp
```

### Step 2: Create virtual environment (recommended)
```text
python -m venv .venv
```
Activate it:
```text
On Windows
.venv\Scripts\activate

On Mac/Linux
source .venv/bin/activate
```
### Step 3: Install dependencies
```text
pip install -r requirements.txt
```

### Step 4: Run all tests
```text
pytest testCases/ -v --html=Reports/report.html
```

### Step 5: Run a single test file
```text
pytest testCases/test_loginPage_ddt.py -v
```

### Alternative: One-click execution
```text
Double-click run.bat
```

## Key Features
- Scalable Page Object Model (POM) design
- Robust Data-Driven Testing (DDT) using external datasets
- Automatic screenshots on failure
- HTML reporting for easy stakeholder review
- Clean configuration management (no hardcoded values)
- Parallel execution support for faster test cycles

## Why This Framework Matters for Senior/Staff QA Roles
- Demonstrates an automation-first mindset
- Built for scalability and maintainability
- Validates critical data workflows (login, customer data)
- Easily integrable into CI/CD pipelines
- Aligns with enterprise and financial system testing standards

# Author
**Jay Raj Prakash**
ISTQB Advanced Level (CTAL-TAE) Certified
```text

📧 jayrajprakash@outlook.com
🔗 [GitHub Profile](https://github.com/click2jay1)
📍 Greater Seattle Area, WA
```
