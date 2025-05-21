from fastapi import FastAPI
from fastapi_mcp import FastApiMCP
from pydantic import BaseModel
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig

app = FastAPI()
mcp = FastApiMCP(app)
mcp.mount()

class CrawlRequest(BaseModel):
    url: str

@app.post("/crawl/", operation_id="crawl_website")
async def crawl_website(request: CrawlRequest):
    browser_config = BrowserConfig()
    crawler_config = CrawlerRunConfig()

    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(
            config=crawler_config,
            url=request.url
        )
        return result.markdown

mcp.setup_server()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)