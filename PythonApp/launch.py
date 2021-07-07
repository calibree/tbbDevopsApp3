from flask import Flask
from flask import jsonify
helloworld = Flask(__name__)

data = {
  "users": [
    {
      "username": "Cansu",
      "mail": "cansutest1@test.com"
    },
    {
      "username": "Satici",
      "mail": "cansutest2@test.com"
    },
    {
      "status": "DevOps Engineer..",
      "source": "www.test.com"
    }
  ]
}

@helloworld.route("/data")
def run():
    return jsonify(data)
if __name__ == "__main__":
    helloworld.run(host="0.0.0.0", port=int("5000"), debug=True)
