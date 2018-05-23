from flask import Flask, render_template
import pymongo
# Create an instance of our Flask app.
app = Flask(__name__)

# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
db = client.costa_rica_db

# Set route
@app.route('/')
def index():
    # Store the entire team collection in a list
    item = list(db.items.find())
    print(item)

    # Return the template with the teams list passed in
    return render_template('index.html', dict=item)


if __name__ == "__main__":
    app.run(debug=True)



