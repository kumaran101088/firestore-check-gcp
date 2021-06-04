from google.cloud import firestore
from flask import Flask, jsonify

# GOOGLE_APPLICATION_CREDENTIALS = r'no-sql-flask-65ed8eb492af.json'

## Project ID is determined by the GCLOUD_PROJECT environment variable
# db = firestore.Client()

# doc_ref = db.collection('users').document('aturing')
# doc_ref.set({
#     'first': 'John',
#     'last': 'Doe'
# })

# users_ref = db.collection('people')
# docs = users_ref.stream()

# for doc in docs:
#     print(doc.to_dict())

app = Flask(__name__)

@app.route('/')
def index():
    db = firestore.Client()
    users_ref = db.collection('people')
    docs = users_ref.stream()
    people = {'people' : [doc.to_dict() for doc in docs]}
    return jsonify(people), 200

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8080)