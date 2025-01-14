from flask import Flask, request, jsonify
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from config import Config

app = Flask(__name__)

# Database setup
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

@app.route('/earthquake/<int:id>', methods=['GET'])
def get_earthquake_by_id(id):
    """
    Fetch a single earthquake record by ID.
    """
    try:
        query = text("SELECT * FROM quakedb WHERE time=:id")
        result = session.execute(query, {'id': id}).fetchone()
        if result:
            return jsonify(dict(result)), 200   
        else:
            return jsonify({"error": "Record not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
