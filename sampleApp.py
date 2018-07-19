from flask import Flask, render_template, request
from datetime import datetime
from horoscopeapi import get_horoscope, zodiac_sign

# This is create instance of Flask. app is variable
app = Flask("MyApp")


# Default route his method will be called when you hit http://127.0.0.0:5000/
@app.route("/")
def home():
    return render_template(
        "home.html")  # render_template method is a special function flask which redirect to the html file mentioned in the paramter


# This method will be called when you hit http://127.0.0.0:5000/writeanythinghere
# This is an example when you want to hit a URL with Paramaters. This is called GET request.
@app.route("/<message>")
def hello_Name(message):
    return render_template("printmessage.html",
                           message=message.title())  # This example take additional paramter which can be passed to the html


# This method is internal method. This can only be called in this python code.
# This menthod is being call from below
def calculate_generation(year_parameter):
    result = ''

    if year_parameter < 1996:
        result = 'Classic'
    if year_parameter in range(1966, 1976):
        result = 'X'
    elif year_parameter in range(1977, 1994):
        result = 'Y'
    elif year_parameter in range(1995, 2012):
        result = 'Z'

    else:
        result = 'IoT'
    return result


# This metho is wcalled when you hit http://127.0.0.0:5000/gen
# But this method is defined as "POST" which means there are paramter or Form object is sent from the webpage.
# e.g from home.html - when submit is part of a form so any fields defined inside the html tag <Form> their values
# are also sent to the backend. These values can we excessed using request object. see first list line of this method
@app.route("/gen", methods=["POST"])
def read_form_data():
    form_data = request.form  # Getting hold of a Form object that is sent from a browser.
    dateOfBirth = form_data["dob"]  # from the form object getting value of dob field.
    date = datetime.strptime(dateOfBirth, '%Y-%m-%d').date()
    month = date.month
    year = date.year
    generation = calculate_generation(year)  # Calling internal method which takes year as a paramter and return text

    return render_template("showmygeneration.html", gen_cohort=generation)


@app.route("/horoscope")
def horoscope():
    return render_template(
        "horoscope.html")  # render_template method is a special function flask which redirect to the html file mentioned in the paramter


@app.route("/myhoroscope", methods=["POST"])
def myhoroscope():
    result = 'No data'
    return render_template("showmyhoroscope.html",
                           data=result)  # render_template method is a special function flask which redirect to the html file mentioned in the paramter


# When you run this file with python this line executed and since app variable is Flask type (defined on line 5)
# when you say run Flask webserver is started. Debug=true is a pramater which allow flask to print messages/error on the command line (console)
if __name__ == "__main__":
    app.run(debug=True)
