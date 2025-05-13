# 🔎 Python Web Scraping and Automation Projects

<div align="center">
  <h1>📊 Remote Job Scraper & 🛒 Amazon Product Link Extractor</h1>
  <img src="https://img.shields.io/badge/python-scripts-blue?style=flat-square" alt="Python Badge"/>
  <img src="https://img.shields.io/badge/automated-email-export-success-brightgreen?style=flat-square" alt="Email Badge"/>
</div>

## 🚀 Project Overview

This repo contains **two simple and effective Python automation scripts**:

1. **RemoteOK Job API Scraper**  
   A Python script that fetches remote job postings using the public API from [remoteok.com](https://remoteok.com/api), processes the data, and exports it to an Excel file. The file is automatically sent via email as an attachment.

2. **Amazon HTML Link Scraper**  
   A basic scraper that reads an Amazon product listing page, extracts product links from the HTML, and stores them in a clean list for further use.

---

## 📁 Project 1: Remote Job API Scraper

### 💡 Features:
- Uses Python's `requests` module to interact with the RemoteOK API.
- Formats and writes job data to an Excel spreadsheet using `xlwt`.
- Automatically sends the `.xls` file via email using `smtplib` and `email.mime`.

### 🧩 Technologies Used:
- `requests`
- `xlwt`
- `smtplib` / `email.mime`

### 📤 Output:
- File: `remote_jobs.xls`
- Sent via Gmail SMTP to the specified recipients.

---

## 📁 Project 2: Amazon HTML Product Link Scraper

### 💡 Features:
- Opens and reads a saved HTML file of Amazon search results.
- Extracts all product URLs by identifying the appropriate `<a>` tags and attributes.
- Stores the links in a list or writes to file.

### 🧩 Technologies Used:
- `BeautifulSoup` (for HTML parsing)
- `re` or string logic (for cleaning)
- Optional: `pandas` or plain Python for storage

---

## 📬 Want to Contribute?

If you have ideas to expand this (e.g., converting to pandas DataFrame, filtering by keywords, building a dashboard), feel free to fork and contribute!

---

## ⚖️ License

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

This project is released under the CC0 Public Domain license. Feel free to use, remix, or share.

---

## 🧠 Author

**Otuekong Emmanuel Udo**  
Python Developer | Web Automation Enthusiast | Data Analyst  
📧 [shieldemmanuel222@gmail.com](mailto:shieldemmanuel222@gmail.com)  
🐙 [GitHub: https://github.com/Shieldemma/
---

## 🌍 Showcase & Comic Diagram

📌 Check out the visual flow diagrams for both projects:
- RemoteOK API Scraper 🧑‍💻📊  
- Amazon HTML Link Scraper 🛒🔗

*(See `/assets/` or image previews for comic-style flow explanation)*

---

