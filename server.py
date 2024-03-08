from flask import Flask
from flask import request, render_template, jsonify
app = Flask(__name__)

data = [
    {
      "id": 1,
      "name": "Hospital Playlist",
      "creators": "Shin Won-ho, Lee Woo-jung",
      "casts": "Cho Jung-seok, Yoo Yeon-seok, Jung Kyung-ho",
      "year": 2020,
      "summary": "Every day is extraordinary for five doctors and their patients inside a hospital, where birth, death and everything in between coexist.",
      "img": "https://0.soompi.io/wp-content/uploads/2020/02/18180122/hospital-playlist11.jpeg"
    },
    {
      "id": 2,
      "name": "Extraordinary Attorney Woo",
      "genres": "Drama, Social Issue, Comedy",
      "creators": "Yoo In-sik, Moon Ji-won",
      "casts": "Park Eun-bin, Kang Tae-oh, Kang Ki-young",
      "year": 2022,
      "summary": "Brilliant attorney Woo Young-woo tackles challenges in the courtroom and beyond as a newbie at a top law firm and a woman on the autism spectrum.",
      "img": "https://m.media-amazon.com/images/M/MV5BMTAzNzlhYjItN2MxZS00ZTg4LWFmZGQtN2I1ZWE5YjgzODY3XkEyXkFqcGdeQXVyNjk1NzU1Mjk@._V1_.jpg"
   },
   {
      "id": 3,
      "name": "The Glory",
      "genres": "Drama, Social Issue",
      "creators": "Kim Eun-sook, An Gil-ho",
      "casts": "Song Hye-kyo, Lee Do-hyun, Lim Ji-yeon",
      "year": 2022,
      "summary": "Years after surviving horrific abuse in high school, a woman puts an elaborate revenge scheme in motion to make the perpetrators pay for their crimes.",
      "img": "https://images.chosun.com/resizer/49LbXaVVpnRL2YGnbhKFbWxL-J4=/540x801/smart/cloudfront-ap-northeast-1.images.arcpublishing.com/chosun/HLXDPZC4EDEZHNGFASHIDBVHSI.jpg"
   },
   {
      "id": 4,
      "name": "Celebrity",
      "genres": "Drama, Romantic",
      "creators": "Kim Cheol-kyu, Kim Yi-young",
      "casts": "Park Gyu-young, Kang Min-hyuk, Lee Chung-ah",
      "year": 2023,
      "summary": "Fame. Money. Power. Seo A-ri achieves social media stardom overnight — but deadly consequences await in this glitzy, gilded world of influencers.",
      "img": "https://d2v0j9zp5u17nn.cloudfront.net/wp-content/uploads/2023/05/31131450/celebrity-poster-1.jpeg"
   },
   {
      "id": 5,
      "name": "Mr. Sunshine",
      "genres": "Drama, Romantic, Political, Historic",
      "creators": "Kim Eun-sook, Lee Eung-bok",
      "casts": "Lee Byung-hun, Kim Tae-ri, Yoo Yeon-seok",
      "year": 2018,
      "summary": "A young boy who ends up in the U.S. after the 1871 Shinmiyangyo incident returns to Korea at a historical turning point and falls for a noblewoman.",
      "img": "https://m.media-amazon.com/images/M/MV5BOWU3MjlmODAtZGU5NS00NmFjLTg1NmItNjU3MjQ5MmM1YWJjXkEyXkFqcGdeQXVyNjc3MjQzNTI@._V1_.jpg"
   },
   {
      "id": 6,
      "name": "Under the Queen's Umbrella",
      "genres": "Drama, Historic",
      "creators": "Kim Hyung-sik, Park Ba-ra",
      "casts": "Kim Hye-soo, Kim Hae-sook, Choi Won-yeong",
      "year": 2022,
      "summary": "A spirited queen tries to rein in her rowdy sons in order to make one of them the next king of Joseon, while her competitors vie to snatch the throne.",
      "img": "https://image.tmdb.org/t/p/original/817aakHe145GTVEi6LzxHSBpbth.jpg"
   },
   {
      "id": 7,
      "name": "Crash Landing on You",
      "genres": "Drama, Romantic, Comedy",
      "creators": "Lee Jung-hyo, Park Ji-eun",
      "casts": "Hyun Bin, Son Ye-jin, Seo Ji-hye",
      "year": 2019,
      "summary": "A paragliding mishap drops a South Korean heiress in North Korea -- and into the life of an army officer, who decides he will help her hide.",
      "img": "https://m.media-amazon.com/images/M/MV5BMzRiZWUyN2YtNDI4YS00NTg2LTg0OTgtMGI2ZjU4ODQ4Yjk3XkEyXkFqcGdeQXVyNTI5NjIyMw@@._V1_.jpg"
   },
   {
      "id": 8,
      "name": "Sweet Home",
      "genres": "Drama, Horror",
      "creators": "Lee Eung-bok, Hong So-ri, Jang Young-woo",
      "casts": "Song Kang, Lee Jin-uk, Lee Si-young",
      "year": 2020,
      "summary": "As humans turn into savage monsters and the world plunges into terror, a handful of survivors fight for their lives — and to hold on to their humanity.",
      "img": "https://m.media-amazon.com/images/M/MV5BNWNjMmQ4MzgtOWY2Ny00MTRhLWI3MmYtOWQ1NWJhMjk4MjQyXkEyXkFqcGdeQXVyNjI4NDY5ODM@._V1_.jpg"
   },
   {
      "id": 9,
      "name": "All of Us Are Dead",
      "genres": "Drama, Horror, Romantic",
      "creators": "Lee JQ, Chun Sung-il, Kim Nam-su",
      "casts": "Park Ji-hu, Yoon Chan-young, Cho Yi-hyun",
      "year": 2022,
      "summary": "A high school becomes ground zero for a zombie virus outbreak. Trapped students must fight their way out — or turn into one of the rabid infected.",
      "img": "https://i.namu.wiki/i/q9mOmRVI-GXPhzMykLV_5gLuA9PSMB4i2mwa7bV7exAjOrhhx3WPgGKHK3cyaHthkMwUbsSrBMeXIybPrL-v0A.webp"
   },
   {
      "id": 10,
      "name": "Squid Game",
      "genres": "Drama, Thriller",
      "creators": "Hwang Dong-hyuk",
      "casts": "Lee Jung-jae, Park Hae-soo, Wi Ha-jun",
      "year": 2021,
      "summary": "Hundreds of cash-strapped players accept a strange invitation to compete in children's games. Inside, a tempting prize awaits — with deadly high stakes.",
      "img": "https://m.media-amazon.com/images/M/MV5BYWE3MDVkN2EtNjQ5MS00ZDQ4LTliNzYtMjc2YWMzMDEwMTA3XkEyXkFqcGdeQXVyMTEzMTI1Mjk3._V1_FMjpg_UX1000_.jpg"
   }
]


@app.route('/')
def main():
   names = [item["name"] for item in data]
   return render_template('index.html', data=data, names=names)
      

@app.route('/search', methods=['GET', 'POST'])
def search():
   names = [item["name"] for item in data]
   search_key = request.args.get('search_key', '')
   results = []
   for item in data:
      if search_key.lower() in item["name"].lower():
         results.append(item)
   return render_template('search.html', results=results, names=names)


@app.route('/view/<id>')
def view(id=1):
   names = [item["name"] for item in data]
   item = get_item_by_id(id)
   if item:
      return render_template('view.html', item=item, names=names)
   else:
      return "Item not found", 404


@app.route('/add', methods=['GET', 'POST'])
def add():
   names = [item["name"] for item in data]
   if request.method == 'POST':
      json_data = request.json
      data.append(json_data)
      return jsonify({"message": "Darama added successfully", "status": "success", "count": len(data)})

   return render_template('add.html', names=names)


@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id=1):
   names = [item["name"] for item in data]
   item = get_item_by_id(id)
   if request.method == 'POST':
      json_data = request.json
      item = json_data
      return jsonify({"message": "Darama edited successfully", "status": "success"})

   return render_template('edit.html', names=names, item=item)


def get_item_by_id(id):
   for data_item in data:
      item = None
      if str(data_item["id"]) == id:
         item = data_item
         break
   return item


if __name__ == '__main__':
   app.run(debug = True)




