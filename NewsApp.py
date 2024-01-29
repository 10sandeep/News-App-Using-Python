import requests
import tkinter as tk

def getNews():
    api_key = "42752b5a77e046d6af5c410d651c469c"
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=" + api_key
    news = requests.get(url).json()

    articles = news["articles"]

    my_articles = []
    my_news = ""

    for article in articles:
        my_articles.append(article["title"])

    for i in range(15):
        my_news = my_news + str(i + 1) + ". " + my_articles[i] + "\n"

    label.config(text=my_news)

canvas = tk.Tk()
canvas.geometry("900x600")
canvas.title("News App")

# Configure button style
button = tk.Button(canvas, text="Reload", command=getNews, font=("Helvetica", 16), relief="flat", bg="#3498db", fg="white")
button.pack(pady=20)

# Configure label style
label = tk.Label(canvas, text="", font=("Helvetica", 14), justify="left")
label.pack(pady=20)

# Initial news fetch
getNews()

canvas.mainloop()
