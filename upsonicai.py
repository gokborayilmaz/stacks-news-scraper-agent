from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse, JSONResponse
from dotenv import load_dotenv
from upsonic import Agent, Task, ObjectResponse
from upsonic.client.tools import BrowserUse

# Load environment variables
load_dotenv()

app = FastAPI(title="Stock News Agent")

# Initialize the AI agent
news_agent = Agent("Stock News Scraper", model="azure/gpt-4o", reflection=True)

# Define response format for stock news
class StockNews(ObjectResponse):
    headline: str
    source: str
    link: str

class StockNewsList(ObjectResponse):
    news: list[StockNews]

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Stock News Scraper</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-gray-100 flex justify-center items-center h-screen">
        <div class="bg-white p-8 rounded-lg shadow-lg w-[40rem]">
            <h1 class="text-2xl font-bold text-center mb-4">📈 Stock News Scraper</h1>
            <input id="stock_symbol" type="text" placeholder="Enter stock symbol (e.g., TSLA)" class="w-full p-2 border rounded mb-4">
            <button onclick="fetchNews()" class="bg-blue-500 text-white px-4 py-2 rounded w-full">Get News</button>
            <div id="result" class="mt-4 text-sm text-gray-800 bg-gray-50 p-4 rounded overflow-y-auto h-64"></div>
        </div>
        <script>
            async function fetchNews() {
                const stock_symbol = document.getElementById("stock_symbol").value;
                if (!stock_symbol) {
                    alert("Please enter a stock symbol.");
                    return;
                }
                const response = await fetch(`http://127.0.0.1:8000/get_stock_news?symbol=${encodeURIComponent(stock_symbol)}`);
                const data = await response.json();
                document.getElementById("result").innerText = JSON.stringify(data, null, 2);
            }
        </script>
    </body>
    </html>
    """

@app.get("/get_stock_news", response_class=JSONResponse)
async def get_stock_news(symbol: str = Query(..., title="Stock Symbol")):
    """Fetches the latest news related to a given stock symbol."""
    try:
        news_task = Task(
            f"Search for the latest news articles related to {symbol} stock and return headlines with sources and links.",
            tools=[BrowserUse],
            response_format=StockNewsList
        )
        news_agent.do(news_task)
        
        return {"news": news_task.response.news if news_task.response else []}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
