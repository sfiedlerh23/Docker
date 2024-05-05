import pandas as pd
from flask import Flask, render_template
import os
from dotenv import load_dotenv
import matplotlib.pyplot as plt

load_dotenv() 
app = Flask(__name__)

# Beispielwert für 'count' für alle Routen
def get_count():
    return 100

@app.route('/')
def hello():
    count = get_count()  # 'count' für die Homepage
    return render_template('hello.html', count=count)

@app.route('/hello.html')
def hello_page():
    count = get_count()  # 'count' für /hello.html
    return render_template('hello.html', count=count)

@app.route('/titanic.html')
def titanic():
    titanic_data = pd.read_csv('titanic.csv')
    titanic_table = titanic_data.head().to_html(index=False)

    # Balkendiagramm erstellen
    survived_sex = titanic_data.groupby(['sex', 'survived']).size().unstack()
    survived_sex.plot(kind='bar')
    plt.xlabel('Sex')
    plt.ylabel('Count')
    plt.title('Survival by Sex')
    plt.savefig('static/survival_chart.png')  # Speichern Sie das Diagramm als Bild
    plt.close()  # Schließen Sie das Diagramm, um Speicher freizugeben

    count = get_count()  # 'count' für /titanic.html
    return render_template('titanic.html', titanic_table=titanic_table, count=count)

@app.route('/about.html')
def about():
    count = get_count()  # 'count' für /about.html
    return render_template('about.html', count=count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
