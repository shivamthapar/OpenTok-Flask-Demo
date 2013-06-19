from flask import Flask, redirect, url_for,render_template
import OpenTokSDK

app = Flask(__name__)

app.config.from_object(__name__)

api_key = ""        # Replace with your OpenTok API key.
api_secret = ""     # Replace with your OpenTok API secret.

opentok_sdk = OpenTokSDK.OpenTokSDK(api_key, api_secret)

@app.route('/')
def index():
	session_properties = {OpenTokSDK.SessionProperties.p2p_preference: "disabled"}
	session = opentok_sdk.create_session(None, session_properties)
	url= url_for('chat',session_id=session.session_id)
	return redirect(url)

@app.route('/<session_id>')
def chat(session_id):
 	token=opentok_sdk.generate_token(session_id)
 	return render_template('chat.html', api_key= api_key, session_id=session_id, token=token)

if __name__ == '__main__':
	app.run()