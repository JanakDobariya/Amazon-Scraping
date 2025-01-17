# 🛒 Amazon Scraping: Extract Product Details from Amazon Effortlessly 📊

<p align="right">

<a href="https://github.com/JanakDobariya/">
<img src="https://badges.pufler.dev/visits/JanakDobariya/Amazon-Scraping?label=VISITOR&style=for-the-badge&logoColor=FFFFFF&color=purple&labelColor=640464&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9IndoaXRlIiB2ZXJzaW9uPSIxLjEiIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld0JveD0iMCAwIDE2IDE2IiBjbGFzcz0ib2N0aWNvbiBvY3RpY29uLWV5ZSIgYXJpYS1oaWRkZW49InRydWUiPjxwYXRoIGQ9Ik04IDJjMS45ODEgMCAzLjY3MS45OTIgNC45MzMgMi4wNzggMS4yNyAxLjA5MSAyLjE4NyAyLjM0NSAyLjYzNyAzLjAyM2ExLjYyIDEuNjIgMCAwIDEgMCAxLjc5OGMtLjQ1LjY3OC0xLjM2NyAxLjkzMi0yLjYzNyAzLjAyM0MxMS42NyAxMy4wMDggOS45ODEgMTQgOCAxNGMtMS45ODEgMC0zLjY3MS0uOTkyLTQuOTMzLTIuMDc4QzEuNzk3IDEwLjgzLjg4IDkuNTc2LjQzIDguODk4YTEuNjIgMS42MiAwIDAgMSAwLTEuNzk4Yy40NS0uNjc3IDEuMzY3LTEuOTMxIDIuNjM3LTMuMDIyQzQuMzMgMi45OTIgNi4wMTkgMiA4IDJaTTEuNjc5IDcuOTMyYS4xMi4xMiAwIDAgMCAwIC4xMzZjLjQxMS42MjIgMS4yNDEgMS43NSAyLjM2NiAyLjcxN0M1LjE3NiAxMS43NTggNi41MjcgMTIuNSA4IDEyLjVjMS40NzMgMCAyLjgyNS0uNzQyIDMuOTU1LTEuNzE1IDEuMTI0LS45NjcgMS45NTQtMi4wOTYgMi4zNjYtMi43MTdhLjEyLjEyIDAgMCAwIDAtLjEzNmMtLjQxMi0uNjIxLTEuMjQyLTEuNzUtMi4zNjYtMi43MTdDMTAuODI0IDQuMjQyIDkuNDczIDMuNSA4IDMuNWMtMS40NzMgMC0yLjgyNS43NDItMy45NTUgMS43MTUtMS4xMjQuOTY3LTEuOTU0IDIuMDk2LTIuMzY2IDIuNzE3Wk04IDEwYTIgMiAwIDEgMS0uMDAxLTMuOTk5QTIgMiAwIDAgMSA4IDEwWiI+PC9wYXRoPjwvc3ZnPg==">
</a> 

</p>

## Overview
Amazon Scraping is a Python project that automates the extraction of product information, such as names and prices, from Amazon's search results. By utilizing requests and BeautifulSoup, the script scrapes data from multiple pages and saves it into a CSV file for further analysis.

## Key Features
- *🔍 Multi-Page Scraping*: Scrapes product details from multiple pages of Amazon search results.
- *📄 CSV Output*: Saves extracted data (product names and prices) in a structured CSV format.
- *🔗 Dynamic Pagination*: Automatically handles URLs for navigating through pages.
- *✅ Error Handling*: Ensures missing price fields are captured gracefully.

## Tech Stack
- *🐍 Python*: The core language powering the scraper.
- *📦 Libraries Used*:
  - requests: For sending HTTP requests and fetching HTML content.
  - BeautifulSoup (bs4): For parsing and extracting HTML data.
  - pandas: For organizing and exporting the scraped data into a CSV file.

## Installation
1. *Clone the repository*:
   bash
   git clone https://github.com/JanakDobariya/Amazon-Scraping.git
   cd Amazon-Scraping
   

2. *Install dependencies*:
   Make sure Python is installed, then run:
   bash
   pip install -r requirements.txt
   

3. *Run the script*:
   bash
   python amazon.py
   

## Usage
- The script extracts product names and prices from Amazon's search results for the keyword "mobiles."
- Outputs a CSV file (amazon.csv) containing:
  - *Product Name*
  - *Product Price*

### Example Output

![image](https://github.com/user-attachments/assets/103a42cb-5dd7-4efa-83f0-6a03d3e09ad8)



## Important Notes
- *Cookies*: Amazon uses cookies for user-specific content. Make sure to update the cookies in the script for accurate scraping.
- *Headers*: The script uses headers to mimic browser requests and avoid detection.
- *Pagination*: Currently set to scrape 20 pages. Adjust as needed.
- *Legal Compliance*: Ensure scraping adheres to Amazon’s [terms of service](https://www.amazon.in/gp/help/customer/display.html?nodeId=200534380).

## Contributions
Contributions are welcome! If you find a bug or have suggestions for improvement, feel free to fork the repository, make your changes, and submit a pull request.

## Disclaimer
This project is intended for educational purposes only. Ensure compliance with Amazon’s policies and applicable laws while using this script.

---
Happy Scraping! 🚀
