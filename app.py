fr
om flask import Flask, render_template
import raspieats

app= Flask(__name__)

@app.route('/')

def index():
    my_game = raspieats.Game()
    my_game.run()
    return "RaspiGame"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')