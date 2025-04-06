# app.py
from flask import Flask, render_template

app = Flask(__name__)

# Sample data
players = [
    {"name": "Roger Federer", "skill": "Advanced", "image": "federer.jpg"},
    {"name": "Rafael Nadal", "skill": "Advanced", "image": "nadal.jpg"}
]

matches = [
    {"player1": "Federer", "player2": "Nadal", "result": "6-3, 4-6, 7-5"},
    {"player1": "Djokovic", "player2": "Murray", "result": "6-4, 6-4"}
]

nextmatch = [
    {"player1": "Court 1: Ian T & Ron A.", "player2": "Dave S. & Gordon M.", "date": "29-04-2025 at 09:00"},
    {"player1": "Court 2: Craig C. & Richard T.", "player2": "Ivan P. & Ken S.", "date": "29-04-2025 at 09:00"}
]

@app.route('/')
def index():
    return render_template('index.html', players=players, matches=matches, nextmatch=nextmatch)

if __name__ == '__main__':
    app.run(debug=True)
