from flask import Flask, render_template
import pandas as pd
import plotly.express as px

app = Flask(__name__)

# Load the simulated data
data = pd.read_csv('solar_data.csv')

@app.route('/')
def index():
    fig1 = px.line(data, x='Time', y='Irradiance', title='Irradiance over Time')
    fig2 = px.line(data, x='Time', y='Temperature', title='Temperature over Time')
    fig3 = px.line(data, x='Time', y='Voltage', title='Voltage over Time')
    fig4 = px.line(data, x='Time', y='Current', title='Current over Time')

    graphs = [fig1.to_html(full_html=False), fig2.to_html(full_html=False), fig3.to_html(full_html=False), fig4.to_html(full_html=False)]
    return render_template('index.html', graphs=graphs)

if __name__ == '__main__':
    app.run(debug=True)

