from flask import Flask,render_template,request
import requests
import json

app=Flask(__name__)
app.config['DEBUG']=True

@app.route('/result',methods=['GET','POST'])
def result():
    if request.method=="POST":
        city=request.form.get('city')
        API_KEY ='073bd01b8b193f3dfc7db66c5a7a8c94'
        weather_url=requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_KEY}')
        weather_data=weather_url.json()
        temp=weather_data['main']['temp']-273.15
        return render_template('index.html', data= temp)
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)