from flask import Flask, request, render_template
import pickle
import pandas as pd
from flask_cors import cross_origin

app = Flask(__name__)
model = pickle.load(open("flight_rf.pkl", "rb"))


@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")


@app.route("/predict", methods=["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        Total_Stops = int(request.form["Total_Stops"])
        #print(Total_Stops)
        dep_time = request.form["dep_time"]
        #print(dep_time)
        Journey_day = int(pd.to_datetime(dep_time, format="%Y-%m-%dT%H:%M").day)
        Journey_month = int(pd.to_datetime(dep_time, format="%Y-%m-%dT%H:%M").month)

        Dep_Hour = pd.to_datetime(dep_time, format="%Y-%m-%dT%H:%M").hour
        Dep_min = pd.to_datetime(dep_time, format="%Y-%m-%dT%H:%M").minute

        arrival_time = request.form["arrival_time"]
        #print('arrival_time',arrival_time)
        Arrival_day = int(pd.to_datetime(arrival_time, format="%Y-%m-%dT%H:%M").day)
        Arrival_hour = pd.to_datetime(arrival_time, format="%Y-%m-%dT%H:%M").hour
        Arrival_min = pd.to_datetime(arrival_time, format="%Y-%m-%dT%H:%M").minute

        #print('Arrival_day','Journey_day',Arrival_day,Journey_day)
        if Arrival_day == Journey_day:

            Duration_hours = abs(Arrival_hour - Dep_Hour)
            Duration_mins = abs(Arrival_min - Dep_min)
            #print('debug 1',Duration_hours,Duration_mins)
        else:
            # if flight
            Duration_hours = Arrival_hour + 24 - Dep_Hour
            Duration_mins = abs(Arrival_min - Dep_min)
            #print('debug 2',Duration_hours, Duration_mins)

        #Air Asia = 0
        airline = request.form["airline"]
        #print(airline)
        if airline == 'IndiGo':
            Jet_Airways = 0
            IndiGo = 1
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
        elif airline == 'Air India':
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 1
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
        elif airline == 'Jet Airways':
            Jet_Airways = 1
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
        elif airline == 'SpiceJet':
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 1
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
        elif airline == 'Multiple carriers':
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 1
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
        elif airline == 'GoAir':
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 1
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
        elif airline == 'Vistara':
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 1
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif airline == 'Vistara Premium economy':
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 1
            Trujet = 0

        elif airline == 'Jet Airways Business':
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 1
            Vistara_Premium_economy = 0
            Trujet = 0

        elif airline == 'Multiple carriers Premium economy':
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 1
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif airline == 'Trujet':
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 1
        else:
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0


        # Banglore = 0
        Source = request.form["Source"]
        #print(Source)
        if Source == 'Kolkata':
            Source_Kolkata = 1
            Source_Delhi = 0
            Source_Chennai = 0
            Source_Mumbai = 0
        elif Source == 'Delhi':
            Source_Kolkata = 0
            Source_Delhi = 1
            Source_Chennai = 0
            Source_Mumbai = 0
        elif Source == 'Chennai':
            Source_Kolkata = 0
            Source_Delhi = 0
            Source_Chennai = 1
            Source_Mumbai = 0
        elif Source == 'Mumbai':
            Source_Kolkata =0
            Source_Delhi =0
            Source_Chennai =0
            Source_Mumbai = 1
        else:
            Source_Kolkata = 0
            Source_Delhi = 0
            Source_Chennai = 0
            Source_Mumbai = 0


        # Banglore = 0
        Destination = request.form["Destination"]
        print(Destination)
        if Destination == 'Kolkata':
            Destination_Kolkata = 1
            Destination_Delhi = 0
            Destination_Cochin = 0
            Destination_Hyderabad = 0
        elif Destination == 'Delhi':
            Destination_Kolkata = 0
            Destination_Delhi = 1
            Destination_Cochin = 0
            Destination_Hyderabad = 0
        elif Destination == 'Cochin':
            Destination_Kolkata = 0
            Destination_Delhi = 0
            Destination_Cochin = 1
            Destination_Hyderabad = 0
        elif Destination == 'Hyderabad':
            Destination_Kolkata =0
            Destination_Delhi =0
            Destination_Cochin =0
            Destination_Hyderabad = 1
        else:
            Destination_Kolkata = 0
            Destination_Delhi = 0
            Destination_Cochin = 0
            Destination_Hyderabad = 0

        prediction = model.predict([[
            Total_Stops,
            Journey_day,
            Journey_month,
            Dep_Hour,
            Dep_min,
            Arrival_hour,
            Arrival_min,
            Duration_hours,
            Duration_mins,
            Air_India,
            GoAir,
            IndiGo,
            Jet_Airways,
            Jet_Airways_Business,
            Multiple_carriers,
            Multiple_carriers_Premium_economy,
            SpiceJet,
            Trujet,
            Vistara,
            Vistara_Premium_economy,
            Source_Chennai,
            Source_Delhi,
            Source_Kolkata,
            Source_Mumbai,
            Destination_Cochin,
            Destination_Delhi,
            Destination_Hyderabad,
            Destination_Kolkata
        ]])
        output = round(prediction[0],2)
        #print(output)
        return render_template('home.html',prediction_text="Your Flight price is Rs. {}".format(output))
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
