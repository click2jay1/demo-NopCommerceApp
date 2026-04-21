

@echo off
:: Move to project directory
cd /d "C:\Selenium-Python\Selenium_Python\demo-NopCommerceApp"

:: Use the LOCAL project python (Replace this path with the one from PyCharm)
"C:\Selenium-Python\Selenium_Python\demo-NopCommerceApp\.venv\Scripts\python.exe" -m pytest -v -s -m "sanity" --html=Reports\report.html .\testCases\ --browser chrome

pause