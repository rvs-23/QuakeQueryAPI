from flask import Flask, request, jsonify
from sqlalchemy import create_engine, text, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import Config

app = Flask(__name__)

# Database setup
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

@app.route('/api/v1/earthquake/<int:id>', methods=['GET'])
def get_earthquake_by_id(id):

    print("======================")
    print(request.headers)
    print("======================")
    if 'X-Sr-Api-Version' in request.headers:
        vsn = request.headers.get("X-Sr-Api-Version")
        if vsn not in ["1", "2"]:
            return jsonify({"error": "Invalid API version"}), 400
    else:
        vsn = "1"
    print(vsn)
    """
    Fetch a single earthquake record by ID.
    """
    try:
        # query = text("SELECT * FROM earthquake_data WHERE id=:id")
        # result = session.execute(query, {'id': id}).fetchone()
        quake = session.query(EarthquakeData).filter(EarthquakeData.id == id).first()
        print(quake)
        if quake:
            if vsn == "1":
                return jsonify(row2dict(quake)), 200
            elif vsn == "2":
                return jsonify(row2dict(quake)), 202
        else:
            return jsonify({"error": "Record not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))

    return d


class EarthquakeData(declarative_base()):
    __tablename__ = 'earthquake_data'
    id = Column(Integer, primary_key=True)
    place = Column(String)
    status = Column(String)

if __name__ == '__main__':
    app.run(debug=True)
