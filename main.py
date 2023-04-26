from flask import Flask, render_template, request
import snowfall
app=Flask(__name__)

@app.route('/')
def root():
    markers=[
        {
        'lat':40.573710,
        'lon':-105.081020,
        'popup':'Starting at the CSU CS Building'
        }
    ]
    resorts = snowfall.march_resorts_list
    return render_template('index.html',markers=markers,resorts=resorts )

if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)
