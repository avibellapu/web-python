from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "Bingo go go!"

if __name__ == "__main__":
    app.run()
