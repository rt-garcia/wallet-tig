import firebase_admin
from firebase_admin import App
from firebase_admin import auth
from firebase_admin import credentials
from firebase_admin import messaging
from firebase_admin.exceptions import FirebaseError
from datetime import datetime

cred1 = credentials.Certificate(
    "bitwit-a2ddc-firebase-adminsdk-9n68y-d042451495.json")
app = firebase_admin.initialize_app(cred1)


def trigger():
    try:
        messaging.send(message=messaging.Message(notification=messaging.Notification(
        title="hola", body="chao"), token="eX9r1Am-kK4-nVGdPJ7U5C:APA91bEsvu8KJGzFk0kJdowtGzJCRnIQYvXGb9EYRI1_263NVBHFCH0HHXMfEcUzmQ_513V5U16nM6H1T0cCwixe4s2xmYgnZps87tauGUFNLBIXTwMrzez3Qkc8ZypheCLBtcmizxFk", data={'content-available': "1"}), app=app)
    except FirebaseError as e:
        print(e)

trigger()
