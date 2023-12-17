# -*- coding: utf-8 -*-
from fastapi.responses import HTMLResponse

from app.app_factory import get_application

app = get_application()


@app.get("/", response_class=HTMLResponse)
def root():
    return """
    <html>
        <head>
            <title> ORKGify </title>
        </head>
        <body>
            You shall <span><b>not</b></span> pass!
        </body>
    </html>
    """


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
