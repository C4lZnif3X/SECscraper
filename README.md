# SECscraper

A simple, one-click tool to extract financial data from SEC 10-K and 10-Q filings using the [EDGAR](https://www.sec.gov/edgar.shtml) system.

## ✅ Features
- Automatically pulls the latest 10-K or 10-Q filings
- Extracts core financial metrics from `facts.json`
- Exports results to a readable `.csv`
- Comes with a prebuilt `.exe` launcher for Windows

## 🚀 Quick Start
1. [Download the latest release here](https://github.com/C4lZinfi3X/SECscraper/releases/latest/)
2. Run `sec_scraper_launcher.exe`
3. Enter a stock ticker (e.g. `MSFT`)
4. Output CSV will be saved in your current directory

## 📦 Tech Stack
- Python 3
- Streamlit (frontend)
- Requests, LXML (for SEC scraping)
- PyInstaller (for `.exe` build)

## 🔗 GitHub Release
👉 [Click here to download the Windows executable](https://github.com/C4lZinfi3X/SECscraper/releases/latest/)

---

Let me know if you want to expand this into a full scraper suite or add multi-ticker/historical support.