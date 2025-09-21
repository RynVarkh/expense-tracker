# 💰 Expense Tracker (Python)

A simple **daily expense tracker** written in Python.  
It allows you to **add daily expenses** and stores them in a JSON file with timestamps for easy tracking.

---

## 🚀 Features
- Add daily expenses with a **title** and **amount**
- Stores each expense with **date and time**
- Saves data in a local `expenses.json` file
- Lightweight, beginner-friendly, and easy to use

---

## 🛠️ Requirements
- Python 3.x  
- No external libraries required (`json`, `os`, and `datetime` are built-in)

---

## 📂 Project Structure

├── expenseTracker.py # Main script
├── expenses.json # Auto-created file to store expenses
└── README.md # Project documentation

---

## ▶️ Usage

1. Clone the repository:
```bash
git clone https://github.com/your-username/expense-tracker.git
cd expense-tracker
```

2. Run the script:
```bash
python3 expenseTracker.py
```

3. Enter your expense:
```bash
Title: Lunch
Amount: 150
```

4. Expense is automatically saved to expenses.json with a timestamp.
