# 📈 Stock News Scraper Agent - UpsonicAI

## 📌 Overview
The **Stock News Scraper Agent** is an AI-powered tool that fetches the latest news headlines related to a given stock symbol. Using **BrowserUse**, it searches financial news sources and extracts structured information without the need for API keys or subscriptions.

## 🚀 Features
- 🔍 **Searches the web for the latest stock-related news**
- 📌 **Extracts headlines, sources, and article links**
- ⚡ **No API keys required – fully automated web scraping**
- 🖥 **User-friendly UI for quick searches**
- 🔄 **FastAPI backend for efficient processing**

---
## 🛠 Installation
### 1️⃣ Clone the repository
```bash
git clone <repository-url>
cd <repository-folder>
```
### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
### 3️⃣ Set up environment variables
Create a `.env` file in the project root and configure it:
```
AZURE_OPENAI_API_KEY="your_azure_openai_api_key"
AZURE_OPENAI_ENDPOINT="your_azure_openai_endpoint"
AZURE_OPENAI_MODEL_NAME="azure/gpt-4o"
AZURE_OPENAI_DEPLOYMENT="your_deployment_name"
AZURE_OPENAI_API_VERSION="your_azure_openai_api_version"
```
### 4️⃣ Run the application
```bash
uvicorn upsonicai:app --reload
```
The app will be available at:
```
http://127.0.0.1:8000/
```

---
## 🖥 Usage
### 🔹 UI Access
1. Open `http://127.0.0.1:8000/` in your browser.
2. Enter a stock symbol (e.g., TSLA, AAPL, AMZN).
3. Click **"Get News"** and view the latest stock news.

### 🔹 API Endpoints
#### Get stock news
```http
GET /get_stock_news?symbol=TSLA
```
##### Response format
```json
{
  "news": [
    {
      "headline": "Tesla stock surges after strong earnings report",
      "source": "CNBC",
      "link": "https://www.cnbc.com/tesla-news"
    }
  ]
}
```

---
## 🎯 Tech Stack
- **Python** 🐍
- **FastAPI** ⚡
- **UpsonicAI Framework** 🤖
- **BrowserUse** 🌐
- **TailwindCSS** 🎨 (for UI styling)

---
## 📌 Notes
- This project **does not require API keys** for scraping stock news.
- The AI agent simulates web browsing to fetch stock news.
- Ensure you have **playwright installed** to avoid browser issues:
```bash
playwright install
```

---
## 🤝 Contributing
Feel free to open issues or submit pull requests to improve the Stock News Scraper Agent!

---
## 📜 License
MIT License © 2024 UpsonicAI

---
## 📢 Contact
For inquiries or suggestions, reach out via GitHub or [Twitter](https://twitter.com/yourhandle).

