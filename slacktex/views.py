from flask import Flask, request, jsonify
from models import Slack


app = Flask(__name__)


@app.route("/",  methods=['GET', 'POST'])
def index():
    if not request.args:
        message = """
        Welcome to SlackTeX!
        Check me out on <a href="https://github.com/nicolewhite/slacktex">GitHub</a>.
        """

        return message

    else:
        slack = Slack()
        payload = slack.post_latex_message(request)

        return jsonify(payload), 200
