# Import Modules
import numpy as np
import pandas as pd
from pandas import DataFrame
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
        f"/api/v1.0/station<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/>"
    )


@app.route("/api/v1.0/station")
def station():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all stations"""
    # Query all stations
    results = session.query(Station.station, Station.name).all()

    session.close()

    # Convert list of tuples into normal list
    all_stations = list(np.ravel(results))

    return jsonify(all_stations)


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of measurement data"""
    # Query all data
    results = session.query(Measurement.station, Measurement.date, Measurement.prcp, Measurement.tobs).all()

    session.close()

    # Create a dictionary from the row data and append to a list of precip_data
    precip_data = []
    for station, date, prcp, tobs in results:
        precip_dict = {}
        precip_dict["station"] = station
        precip_dict["date"] = date
        precip_dict["prcp"] = prcp
        precip_dict["tobs"] = tobs
        
        precip_data.append(precip_dict)

    return jsonify(precip_data)

@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """get the data from the most busy station"""
    # Query all data
   
    results = session.query(Measurement.station, Measurement.date, Measurement.prcp, Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= '2016-08-23') and (Measurement.date <= '2017-08-23')

    # Create a dictionary from the row data and append to a list of active_data
    active_data = []
    for station, date, prcp, tobs in results:
        active_dict = {}
        active_dict["station"] = station
        active_dict["date"] = date
        active_dict["prcp"] = prcp
        active_dict["tobs"] = tobs
        
        active_data.append(active_dict)

    return jsonify(active_data)


    session.close()

if __name__ == '__main__':
    app.run(debug=True)

