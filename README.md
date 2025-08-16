# 🛒 E-Commerce Automation Testing Project

This project automates test cases for [SauceDemo](https://www.saucedemo.com/) using **Selenium, PyTest, and ChromeDriver**.  
It validates login, add-to-cart, and checkout workflows, including both **positive** and **negative** test cases.  

## 🚀 Features
- ✅ Positive Test Cases:
  - Valid Login
  - Add Product to Cart
  - Complete Checkout Process
- ❌ Negative Test Cases:
  - Invalid Login Attempt
  - Checkout with Missing Information
- 📊 HTML Reports with `pytest-html`
- 📸 Automatic Screenshots on Test Failures

## 🛠 Tech Stack
- Python 3.12
- Selenium
- PyTest
- PyTest-HTML
- ChromeDriver 139

## ▶️ How to Run
```bash
pip install -r requirements.txt
pytest --html=report.html --self-contained-html
