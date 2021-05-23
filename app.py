# Import Modules
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
database_path = "hawaii.sqlite"
engine = create_engine("sqlite:///{}".format(database_path))

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)
print(Base.classes.keys())

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/station"
    )


@app.route("/api/v1.0/station")
def station():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all stations"""
    # Query all stations
    results = session.query(Station.station).all()

    session.close()

    # Convert list of tuples into normal list
    all_stations = list(np.ravel(results))

    return jsonify(all_stations)


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of passenger data including the name, age, and sex of each passenger"""
    # Query all passengers
    results = session.query(Measurement.station, Measurement.date, Measurement.prcp, Measurement.tobs).all()

    session.close()

    # Create a dictionary from the row data and append to a list of all_passengers
    precip_data = []
    for station, date, prcp, tobs in results:
        precip_dict = {}
        precip_dict["station"] = station
        precip_dict["date"] = date
        precip_dict["prcp"] = prcp
        precip_dict["tobs"] = tobs
        
        precip_data.append(precip_dict)

    return jsonify(precip_data)


if __name__ == '__main__':
    app.run(debug=True)

