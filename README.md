
# SauceDemo Automated Tests

## 🧪 Tools
- Selenium
- Python 3
- Unittest Framework

## ✅ Workflows Covered
1. Login
2. Add product to cart
3. Checkout flow

## ▶️ How to Run
```bash
pip install -r requirements.txt
python -m unittest discover tests/
```

## ⚠️ Challenges Faced
- Dynamic elements loading too fast, requiring time.sleep or better wait strategies
- No CAPTCHA, so easier for test automation (good)
- Need for Page Object Model in real-world scenarios

## 💡 Improvements (Real-World)
- Use Page Object Model for better maintainability
- Add test report generation (e.g., Allure)
- Add cross-browser support via Selenium Grid
