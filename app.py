from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!doctype html>
    <html>
    <head>
        <title>Bin Day</title>
        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
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
            h1 { margin-top: 0; font-size: 1.8rem; }
            p { line-height: 1.5; color: #cbd5f5; }
            input {
                width: 100%;
                padding: 12px;
                border-radius: 6px;
                border: 1px solid #334155;
                margin-top: 12px;
                font-size: 1rem;
            }
            button {
                margin-top: 16px;
                width: 100%;
                background: #6366f1;
                color: white;
                padding: 14px;
                border-radius: 8px;
                border: none;
                font-weight: 600;
                cursor: pointer;
            }
            button:hover { background: #4f46e5; }
        </style>
    </head>
    <body>
        <div class=\"card\">
            <h1>Never forget bin day again</h1>
            <p>Enter your postcode to see your next bin collection.</p>
            <form method=\"post\" action=\"/check\">
                <input name=\"postcode\" placeholder=\"e.g. SW1A 1AA\" required />
                <button type=\"submit\">Check my bin day</button>
            </form>
        </div>
    </body>
    </html>
    """

@app.post("/check", response_class=HTMLResponse)
def check(postcode: str = Form(...)):
    return f"""
    <html><body style='font-family:system-ui;background:#0f172a;color:white;display:flex;justify-content:center;align-items:center;height:100vh;'>
    <div style='background:#020617;padding:32px;border-radius:12px;max-width:420px;'>
        <h2>Postcode: {postcode.upper()}</h2>
        <p>Next collection: <strong>Wednesday – General waste</strong></p>
        <p style='opacity:0.7'>(Hard‑coded for now)</p>
        <a href='/' style='color:#6366f1'>Check another</a>
    </div>
    </body></html>
    """

@app.get("/status")
def status():
    return JSONResponse({"status": "Bin Day app running (deployed)"})
