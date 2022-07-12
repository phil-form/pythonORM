from app import app
import os

port = int(os.environ.get('PORT', 8080))
app.run('0.0.0.0', port=port)
