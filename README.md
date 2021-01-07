<h1 align="center">Python Project Template </h1> <br>
<h2 align="center">🚀 🐍 🚀 🐍 🚀 🐍 🚀 🐍 🚀 🐍 🚀 🐍 </h2> <br>

## Table of Contents

- [About](#about)
- [Benefit](#benefit)
- [Info](#info)
- [Structure](#structure)

## About
A well structured software project is a crucial part of the application for a successful development cycle today. You can clone this github repository to use as a standardized python application template and can easily manage your python projects. 

## Benefit
 Through the unified project structure and layout, you can create effective codes. It is easy to keep your application project consistent and clean.
## Info

https://realpython.com/python-application-layouts/

https://docs.python-guide.org/writing/structure/

## Structure

    .
    │
    ├── env/
    │
    ├── conf/
    │
    ├── lib/
    │
    ├── docs/
    │   ├── concept.txt
    │   ├── app1.md
    │   └── app2.md
    │
    ├── project/
    │   ├── main.py
    │   ├── conf.py
    │   ├── app1/
    │   │   ├── __init__.py
    │   │   ├── app1.py
    │   │   └── helpers.py
    │   │
    │   └── app2/
    │       ├── __init__.py
    │       ├── app2.py
    │       └── helpers.py
    │
    ├── data/
    │   ├── raw/
    │   ├── processed/
    │   └── cleaned/
    │
    ├── sample/
    │   ├── app1/
    │   └── app2/
    │
    ├── tests/
    │   ├── test_main.py
    │   ├── app1/
    │   │   ├── __init__.py
    │   │   ├── test_app1.py
    │   │   └── test_helpers1.py
    │   │
    │   └── app2/
    │       ├── test_app2.py
    │       └── test_helpers2.py
    │
    ├── .gitignore
    ├── LICENSE
    ├── README.md
    └── requirements.txt