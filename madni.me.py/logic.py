from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # Data for dynamic rendering
    data = {
        "projects": ["Vsearch For words"],
        "labs": ["Lab 1", "Lab 2", "Lab 3"],
        "social_links": {
            "LinkedIn": "https://www.linkedin.com/in/madni-vhora",
            "GitHub": "https://github.com/Madni09"
        }
    }
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)



"""from flask import Flask, render_template



app = Flask(__name__) 


@app.route("/") 
def home(): 
	
	return render_template("index.html") 


@app.route("/default") 
def default(): 
	return render_template("layout.html") 




@app.route("/choice/<pick>") 
def choice(pick): 
	if pick == 'variable': 
		return redirect(url_for('var')) 
	if pick == 'if': 
		return redirect(url_for('ifelse')) 
	if pick == 'for': 
		return redirect(url_for('for_loop')) 


if __name__ == "__main__": 
	app.run(debug=False) 
"""