from flask import Flask, render_template
import pymongo

app = Flask(__name__)

# setup mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# connect to mongo db and collection
db = client.dive_sites_db
wks = db.wrecks_obstructs


@app.route("/")
def homepg():
    
    wreck_name = wks.find({"Vessel Terms": "FRENCH KISS"})


    return render_template("index.html", wr_name = wreck_name)




if __name__ == "__main__":
    app.run(debug=True)
