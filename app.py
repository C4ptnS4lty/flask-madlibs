from flask import Flask, render_template, request

from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

@app.route("/")
def ask_questions():
    """Generate and show form to ask for words."""

    prompts = story.prompts

    return render_template("questions.html", prompts = prompts)

@app.route("/")
def show_story():
    """Show results of words in story"""

    text = story.generate(request.args)

    return render_template('story.html', text = text)