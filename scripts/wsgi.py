import sys
sys.path.append("..")
from service import app

if __name__ == "__main__":
    app.run(debug=True)
