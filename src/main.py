# Import necessary classes from Flask and the sandhi library
from flask import Flask, render_template, request
import sandhi
import re

# Initialize the Flask application
app = Flask(__name__, template_folder="../templates")

# Create a single, global instance of the Sandhi class
# This is more efficient than creating it for every request
S = sandhi.Sandhi()

def is_sanskrit(text):
    # This regex checks for common Devanagari (Sanskrit) Unicode range
    # You might need to adjust this based on the specific Sanskrit characters you expect
    sanskrit_pattern = re.compile(r'^[\u0900-\u097F\s]+$')
    return sanskrit_pattern.match(text) is not None

# Define the route for the main page
@app.route('/', methods=['GET', 'POST'])
def home():
    # Initialize variables
    sandhi_result = ""
    first_word = ""
    second_word = ""

    # Check if the form was submitted (i.e., a POST request)
    if request.method == 'POST':
        # Get the words from the form data
        first_word = request.form.get('first_word')
        second_word = request.form.get('second_word')

        # Validate if the input words are in Sanskrit
        if not is_sanskrit(first_word) or not is_sanskrit(second_word):
            return render_template('index.html', error="Please enter only Sanskrit characters.")

        # Ensure both words are provided before calling the sandhi function
        if first_word and second_word:
            # Perform the sandhi operation
            sandhi_result = S.sandhi(first_word, second_word)

    # Render the HTML page and pass the variables to it
    # This happens on both GET (initial page load) and POST (after form submission)
    return render_template('index.html', result=sandhi_result, first=first_word, second=second_word)

# This allows the script to be run directly
if __name__ == '__main__':
    app.run(debug=True)