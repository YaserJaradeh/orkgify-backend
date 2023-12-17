# -*- coding: utf-8 -*-

from app.app_factory import get_application

app = get_application()


def root():
    return """
    <html>
        <head>
            <title> ORKGify </title>
        </head>
        <body>
            You shall not pass!
        </body>
    </html>
    """
