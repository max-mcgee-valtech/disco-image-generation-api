from application import app
import os

# if __name__ == '__main__':    
# if __name__ == '__main__':
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port, debug=False, use_reloader=False)
