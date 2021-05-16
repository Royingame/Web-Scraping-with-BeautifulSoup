from bs4 import BeautifulSoup
import requests
#import csv

source = requests.get("https://coreyms.com/").text
soup = BeautifulSoup(source,"lxml")

#csv_file = open('test_scrape.csv','w')

#csv_writer = csv.writer(csv_file)
#csv_writer.writerow(['headline', 'summary', 'video_link'])

#article = soup.find("article")
#print(article.prettify())

#headline = article.h2.a.text
#print(headline)

#summary = soup.find("div", class_ = "entry-content").p.text
#print(summary)

#vid_url = article.find("iframe", class_ = "youtube-player")["src"]
#print(vid_url)

#vid_id = vid_url.split("/")[4]
#vid_id = vid_id.split("?")[0]
#print(vid_id)

#yt_link = f"https://youtube.com/watch?v={vid_id}"
#print(yt_link)

for article in soup.find_all("article"):
    headline = article.h2.a.text
    print(headline)

    summary = soup.find("div", class_="entry-content").p.text
    print(summary)

    #vid_url = article.find("iframe", class_="youtube-player")["src"]
    #print(vid_url)

    #vid_id = vid_url.split("/")[4]
    #vid_id = vid_id.split("?")[0]
    #print(vid_id)

    #yt_link = f"https://youtube.com/watch?v={vid_id}"
    #print(yt_link)

    #print()

    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']

        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]

        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None

    print(yt_link)

    print()

    #csv_writer.writerow([headline, summary, yt_link])

#csv_file.close()

