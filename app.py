from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!doctype html>
    <html>
    <head>
        <title>Bin Day</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {
                font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
                background: #0f172a;
                color: #e5e7eb;
                display: flex;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
            }
            .card {
                background: #020617;
                border: 1px solid #1e293b;
                border-radius: 12px;
                padding: 32px;
                max-width: 420px;
                width: 100%;
                box-shadow: 0 20px 40px rgba(0,0,0,0.4);
            }
            h1 {
                margin-top: 0;
                font-size: 1.8rem;
            }
            p {
                line-height: 1.5;
                color: #cbd5f5;
            }
            .cta {
                margin-top: 24px;
                display: block;
                text-align: center;
                background: #6366f1;
                color: white;
                padding: 14px;
                border-radius: 8px;
                text-decoration: none;
                font-weight: 600;
            }
            .cta:hover {
                background: #4f46e5;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Never forget bin day again</h1>
            <p>
                Enter your postcode and instantly get your bin collection days.
                Add them straight to your calendar in one click.
            </p>
            <a class="cta" href="/status">Check service status</a>
        </div>
    </body>
    </html>
    """

@app.get("/status")
def status():
    return JSONResponse({"status": "Bin Day app running (deployed)"})
