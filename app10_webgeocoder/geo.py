from flask import  Flask, render_template, request, send_file
import pandas
from werkzeug import secure_filename
from geopy.geocoders import Nominatim

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/success-table/', methods=["POST"])
def success():
    global file
    if request.method=='POST':
        try :
            file=request.files["file"]
        except:
            return render_template("index.html",
            failure="failure.html",
            text="No File Selected! Please Try again.")

        c=pandas.read_csv(file)
        if "address" in c.columns or "Address" in c.columns :
            colname=""
            if "address" in c.columns :
                colname="address"
            elif "Address" in c.columns :
                colname="Address"

            geolocator = Nominatim()
            coor=[(geolocator.geocode(loc)) for loc in c[colname]]
            lat=[]
            long=[]
            for x in coor:
                if x != None :
                    lat.append(x.latitude)
                    long.append(x.longitude)
                else :
                    lat.append(None)
                    long.append(None)
            c["Latitude"]=lat;
            c["Longitude"]=long;
            return render_template("index.html",
            btn="success-table.html",
            table=c.to_html())

            # file.save(secure_filename("uploaded"+file.filename))
        else:
            return render_template("index.html",
            failure="failure.html",
            text="No Address or address column in data! Please Try again with another file.")


@app.route("/download")
def download():
    print(file.filename)
    return send_file(file.filename, attachment_filename="yourfile.csv", as_attachment=True)




if __name__=="__main__" :
    app.run(debug=True)
