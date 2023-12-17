# ORKGify Backend
The core backend for the ORKGify game

## How to run
You need to create a virtual environment and install the dependencies, then run via uvicorn. You can do this by running the following commands:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pre-commit install
uvicorn app.main:app --reload
```
