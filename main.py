from fastapi import FastAPI
from fastapi_mcp import FastApiMCP
import json

app = FastAPI()
mcp = FastApiMCP(app)
mcp.mount()

@app.get("/users/", operation_id="get_users")
async def get_users():
    return json.dumps(["Rizki", "Luki", "Muhammad"])

mcp.setup_server()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)