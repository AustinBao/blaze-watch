import os
from app import app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Railway PORT or default to 8000
    app.run(host="0.0.0.0", port=port)

