from flask import Flask
from datetime import datetime
from src.data import load_descriptions
from src.sommelier import AI_Sommelier
app = Flask(__name__)

#descriptions = load_descriptions()
#sommelier = AI_Sommelier(descriptions, subset=10_000)

@app.route('/')
def homepage():
    # the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")
	# the_time = "my time" 
	
    return """
    <h1>AI Sommelier</h1>
    <p>It is currently {time}.</p>

    # <img src="http://loremflickr.com/600/400/wine" />
	
    """.format(time="five o'clock somewhere")

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)



# <img src="http://loremflickr.com/600/400" />

# <img src="https://github.com/zwrankin/heroku-basic-flask/blob/master/readme_assets/images/download-heroku-toolbelt.png" />
	