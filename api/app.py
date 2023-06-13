#!/usr/bin/python3
"""This module start our application for our api"""
from flask import Flask, make_response, jsonify
from sqlalchemy.exc import NoResultFound, IntegrityError
from flask_mail import Mail
from flask_cors import CORS
from models import storage
from api.views import app_view

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = "db4e1ce9-7acd-4b12-ad39-7747070331c5"
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'muhammadjamiuabdulrazak@gmail.com'
app.config['MAIL_DEFAULT_SENDER'] = 'muhammadjamiuabdulrazak@gmail.com'
app.config['MAIL_MAX_EMAILS'] = None
app.config['MAIL_ASCII_ATTACHMENTS'] = False
app.config['MAIL_OAUTH_CLIENT_ID'] = '891474599223-ld9sakffrp7l625e9pbmsc8ltvsmtah9.apps.googleusercontent.com'
app.config['MAIL_OAUTH_CLIENT_SECRET'] = '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'
app.config['MAIL_OAUTH_AUTH_URL'] = 'https://accounts.google.com/o/oauth2/auth'
app.config['MAIL_OAUTH_TOKEN_URL'] = 'https://accounts.google.com/o/oauth2/token'
app.config['MAIL_OAUTH_SCOPE'] = 'https://mail.google.com/'
mail = Mail(app)
cors = CORS(app)


@app.teardown_appcontext
def close_db(error):
    """Close db session"""
    storage.close()

@app.errorhandler(404)
def not_found(error):
    """Handle 404 error and return a json"""
    return make_response(jsonify({'error': "Not found"}), 404)

@app.errorhandler(NoResultFound)
def handle_no_result_found_error(error):
    """"Handle result not found error"""
    error_response = {
        'error': 'ID Not Found',
        'message': 'The requested ID was not found in the database.'
    }
    return jsonify(error_response), 404

@app.errorhandler(IntegrityError)
def handle_integrity_error(error):
    # Extract the error message from the exception
    error_message = str(error.orig)

    # Check if it's a duplicate entry error
    if 'Duplicate entry' in error_message:
        print("duplicate entry")
        # Parse the duplicate entry value from the error message
        duplicate_entry = error_message.split("'")[1]

        # Create a custom error response
        error_response = {
            'error': 'Duplicate Entry',
            'message': f"The value '{duplicate_entry}' already exists in the database."
        }
        return jsonify(error_response), 400

    # For other types of IntegrityErrors, you can provide a generic error response
    error_response = {
        'error': 'Integrity Error',
        'message': 'An integrity constraint violation occurred in the database.'
    }
    print(error_message)
    return jsonify(error_response), 400

if __name__ == "__main__":
    app.register_blueprint(app_view)
    app.run(host="0.0.0.0", port="5001", threaded=True)
