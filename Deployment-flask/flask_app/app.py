import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import matplotlib.pyplot as plt
import pandas
import squarify
import missingno as msno
import seaborn as sns
import gmplot
from mpl_toolkits.basemap import Basemap



app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
random1 = pickle.load(open('random.pkl', 'rb'))
df = pandas.read_csv('cond.csv')
X=df[['so2','no2','rspm','spm']].values
y=df[['Condition']].values



m = Basemap(projection='mill',
            llcrnrlat = 7,
            llcrnrlon = 65,
            urcrnrlat = 37,
            urcrnrlon = 100,
            resolution='l')



lati=[17.38714,
 26.148043,
 24.833946,
 30.741482,
 28.653229,
 23.033863,
 28.205523,
 30.8381,
 12.972442,
 9.939093,
 18.516726,
 21.146633,
 19.997454,
 19.970324,
 19.21833,
 19.07609,
 24.813967,
 30.900965000000006,
 31.326015,
 30.663738,
 25.1695181,
 26.92207,
 27.560932,
 24.879999,
 26.263863,
 24.57127,
 13.067439,
 27.17667,
 26.85,
 26.449923,
 28.535517,
 28.6692,
 22.59577,
 22.572645]

longi=[78.49168399999998,
 91.731377,
 92.779282,
 76.768066,
 77.308601,
 72.585022,
 76.795311,
 76.9585,
 77.58064300000002,
 76.270523,
 73.856255,
 79.08886,
 73.789803,
 79.30336,
 72.978088,
 72.877426,
 93.950279,
 75.857277,
 75.57618000000002,
 76.300042,
 75.854838,
 75.778885,
 76.625015,
 74.629997,
 73.008957,
 73.691544,
 80.237617,
 78.008072,
 80.949997,
 80.33187099999998,
 77.391029,
 77.4538,
 88.263641,
 88.363892]



typ=[1,
 1,
 2,
 4,
 3,
 4,
 4,
 4,
 1,
 2,
 3,
 1,
 4,
 1,
 1,
 4,
 2,
 3,
 1,
 4,
 4,
 1,
 1,
 4,
 1,
 1,
 1,
 3,
 1,
 1,
 1,
 4,
 4,
 4]


air_data =pandas.read_csv('cond.csv',encoding='latin1')
air_data.spm = air_data['spm'].fillna(air_data['spm'].mean())
air_data.rspm = air_data['rspm'].fillna(air_data['rspm'].mean())
air_data.so2 = air_data['so2'].fillna(air_data['so2'].mean())
air_data.no2 = air_data['no2'].fillna(air_data['no2'].mean())



@app.route('/')
def home():
    return render_template('index(main).html')

@app.route('/knn')
def homee():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])


def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    return render_template('index.html', prediction_text=' {}'.format(prediction))



@app.route('/random')


def random():
    return render_template('index(random).html')

@app.route('/predict1',methods=['POST'])
def predict1():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = random1.predict(final_features)

    return render_template('index1.html', prediction_text='Label $ {}'.format(prediction))




@app.route('/randomReg')
def randomReg():
    return render_template('index(randomRegresion).html')

@app.route('/predict3',methods=['POST'])
def predict2():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = RandomReg.predict(final_features)

    return render_template('index(randomRegresion).html', prediction_text='Label $ {}'.format(prediction))




@app.route('/figure')
def figure():
    '''
    For rendering results on HTML GUI
    '''
    so2_level  = air_data.groupby(['state']).mean()['so2'].sort_values(ascending = False).to_frame()
    sns_plot=sns.barplot(x = 'so2', y = so2_level.index,data = so2_level,palette='inferno')
    fig = sns_plot.get_figure()
    fig.savefig("static/images/new_plot.png")

    return render_template('fig.html',name = 'new_plot', url ='static/images/new_plot.png')
    #return render_template('index(random).html')



@app.route('/map')
def mapp():
    '''
    For rendering results on HTML GUI
    '''
    gmap3 = gmplot.GoogleMapPlotter(30.3164945,
                                78.03219179999999, 8)
    gmap3.heatmap( lati, longi )


    return render_template('pleasework.html')

@app.route('/source')
def sourcee():
    m.drawcoastlines()
    m.drawcountries(linewidth=1)
    m.etopo()

    i=0
    a=0
    b=0
    c=0
    d=0
    while(i<34):
        xpt, ypt = m(longi[i], lati[i])
        if(typ[i]==1):
            if(a==0):
                m.plot(xpt, ypt, 'co', color='red', markersize=7, label='RRO' )
                a=a+1
            else:
                m.plot(xpt, ypt, 'co', color='red', markersize=7 )
        if(typ[i]==2):
            if(b==0):
                m.plot(xpt, ypt, 'co', color='black', markersize=7, label='RO' )
                b=b+1
            else:
                m.plot(xpt, ypt, 'co', color='black', markersize=7 )
        if(typ[i]==3):
            if(c==0):
                m.plot(xpt, ypt, 'co', color='blue', markersize=7, label='R' )
                c=c+1
            else:
                m.plot(xpt, ypt, 'co', color='blue', markersize=7 )
        if(typ[i]==4):
            if(d==0):
                m.plot(xpt, ypt, 'co', color='white', markersize=7,label='I')
                d=d+1
            else:
                m.plot(xpt, ypt, 'co', color='white', markersize=7)
        i=i+1
        plt.legend()
        plt.title('Pollution Hotspots')
        plt.savefig('static/images/source.png')

    return render_template('source.html',name = 'source', url ='static/images/source.png')









@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)


if __name__ == "__main__":
    app.run(debug=True)
