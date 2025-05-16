# eBay Product Scraper
# 🛒 eBay Product Scraper with Scrapy

This project is a simple yet effective Scrapy spider that scrapes **laptop listings** from eBay using **XPath-based HTML parsing**.

---

## 🚀 Features

- Scrapes **product title**, **price**, **URL**, **images**, and **pagination link**
- Scrapes **up to 2 pages** of search results not to get blocked other wise use poxies
- Clean CSV or JSON output
- Handles basic bot protection by using headers

---

## 📂 Output Sample

| Product_title | Product_Price | Product_link | Product_images |
|---------------|---------------|---------------|----------------|
| HP Elitebook | $129.99 | https://ebay.com/... | img1.jpg, img2.jpg |

---

## 📦 Requirements

```bash
pip install scrapy
