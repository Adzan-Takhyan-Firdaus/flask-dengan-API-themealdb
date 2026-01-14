# 🍳 Food Recipe App (Flask Based)

> A dynamic web application to explore global food recipes, built with **Flask** and **TheMealDB API**.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Framework](https://img.shields.io/badge/Framework-Flask-green?style=flat&logo=flask)
![Bootstrap](https://img.shields.io/badge/Frontend-Bootstrap_4-purple?style=flat&logo=bootstrap)

## 📖 About The Project
This project was developed as a Final Exam (UAS) assignment for the **Object-Oriented Programming (OOP)** course. The application allows users to search for recipes, view detailed ingredients (processed from raw JSON), filter meals by categories, and view the development team profile.

The app fetches data in real-time from the public **TheMealDB API**, demonstrating the implementation of RESTful API consumption in a Python Flask environment.

## ✨ Key Features
* **Dynamic Home Page**: Displays random meal recommendations and search functionality.
* **Smart Ingredient Parsing**: Converts scattered ingredient data from the API into a clean, readable list using Python logic.
* **Category Filtering**: Browse meals by categories (Beef, Chicken, Seafood, Vegetarian, etc.) with dynamic routing.
* **Interactive UI**: Responsive design using Bootstrap 4 with custom gradient styling.
* **Team Page**: A dynamic "About Us" page rendering team members' profiles.

## 🛠️ Tech Stack
* **Backend**: Python, Flask (Microframework)
* **API**: [TheMealDB](https://www.themealdb.com/api.php) (Public JSON API)
* **Frontend**: HTML5, CSS3, Bootstrap 4, Jinja2 Templating
* **Libraries**: `requests`, `urllib3`

## 📂 Project Structure
```text
/your-project-folder
│
├── static/              # CSS, Images, and Assets
├── templates/           # HTML Templates (Jinja2)
│   ├── index.html       # Home & Category Filter Page
│   ├── product.html     # Detail Recipe Page
│   ├── categories.html  # Category Selection Page
│   └── about.html       # Team Profile Page
│
├── app.py               # Main Application Logic (Routes & API Calls)
├── requirements.txt     # List of Dependencies
└── README.md            # Project Documentation
