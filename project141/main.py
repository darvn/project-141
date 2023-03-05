from flask import Flask, jsonify, request
import pandas as pd

articles_data = pd.read_csv('articles.csv')
all_articles = articles_data[['url' , 'title' , 'text' , 'lang' , 'total_events']]
liked_articles = []
not_liked_articles = []

app = Flask(__name__)

def assign_val():
    m_data = {
        "url": all_articles.iloc[0,0],
        "title": all_articles.iloc[0,1],
        "text": all_articles.iloc[0,2] or "N/A",
        "lang": all_articles.iloc[0,3],
        "total_events": all_articles.iloc[0,4]
    }
    return m_data

# API to display first article
@app.route("/get-article")
def get_article():
    first_article = assign_val()
    return jsonify({
        "data":first_article,
        "status":"success"
    })



# API to move the article into liked articles list
@app.route("/liked-article")
def liked_article():
    first_article = assign_val()
    liked_articles.append(first_article)
  
    return jsonify({
        "status":"success",
        "data" : liked_articles
    })


# # API to move the article into not liked articles list
@app.route("/unliked-article")
def unliked_article():

    first_article = assign_val()
    not_liked_articles.append(first_article)

# run the application
if __name__ == "__main__":
    app.run()