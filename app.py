# Creator: Athokpam Yaraba Luwang
# License: Apache 2.0

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()

# Tell FastAPI where our HTML file is
templates = Jinja2Templates(directory="templates")

# Route 1: Serve the HTML frontend
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html"
    )

# Route 2: A mock REST API endpoint
@app.get("/api/chat")
async def mock_chat():
    return {
        "status": "success",
        "message": "Hello from AWS App Runner (FastAPI)! This is your mock API response.",
        "bot_name": "FastAPIPracticeBot"
    }

if __name__ == '__main__':
    # Run the app locally on port 8080 (App Runner default)
    uvicorn.run(app, host='0.0.0.0', port=8080)
