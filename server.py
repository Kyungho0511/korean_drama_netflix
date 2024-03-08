from flask import Flask
from flask import request, render_template, jsonify
app = Flask(__name__)

data = [
    {
      "id": 1,
      "name": "Hospital Playlist",
      "genres": "Drama, Medical, Comedy, Romantic",
      "creators": "Shin Won-ho, Lee Woo-jung",
      "casts": "Cho Jung-seok, Yoo Yeon-seok, Jung Kyung-ho",
      "year": 2020,
      "summary": "Hospital Playlist follows the lives of five doctors in their forties, Lee Ik-jun, Ahn Jeong-won, Kim Jun-wan, Yang Seok-hyeong and Chae Song-hwa, working at the Yulje Medical Centre, who first became friends during medical school. Lee Ik-jun is an assistant professor of general surgery specializing in liver transplants and a single father to his only son Woo-joo (Kim Joon) after getting divorced from his absent wife. His cheerful charisma allows him to connect with both patients and doctors, making him a popular figure in the hospital.",
      "img": "https://0.soompi.io/wp-content/uploads/2020/02/18180122/hospital-playlist11.jpeg"
    },
    {
      "id": 2,
      "name": "Extraordinary Attorney Woo",
      "genres": "Drama, Social Issue, Comedy",
      "creators": "Yoo In-sik, Moon Ji-won",
      "casts": "Park Eun-bin, Kang Tae-oh, Kang Ki-young",
      "year": 2022,
      "summary": "Extraordinary Attorney Woo tells the story of Woo Young-woo, an autistic lawyer who is raised by her single father. She grows up with one friend at school, Dong Geu-ra-mi, an oddball girl who protects her from school bullies. She graduates at the top of her law school class at Seoul National University. Because she is autistic, law firms refuse to hire her. However, through a connection of her father's, she obtains her first job at Hanbada, a large Seoul law firm. Attorney Woo's intelligence and photographic memory help her to become an excellent lawyer, as she is able to recall laws and everything she reads, sees, or hears perfectly.",
      "img": "https://m.media-amazon.com/images/M/MV5BMTAzNzlhYjItN2MxZS00ZTg4LWFmZGQtN2I1ZWE5YjgzODY3XkEyXkFqcGdeQXVyNjk1NzU1Mjk@._V1_.jpg"
   },
   {
      "id": 3,
      "name": "The Glory",
      "genres": "Drama, Social Issue",
      "creators": "Kim Eun-sook, An Gil-ho",
      "casts": "Song Hye-kyo, Lee Do-hyun, Lim Ji-yeon",
      "year": 2022,
      "summary": "Moon Dong-eun, a former victim of school violence plans and seeks revenge on her bullies after taking up a job as a homeroom teacher at the elementary school of the bully leader's child (Ha Ye-sol).[5] Some scenes are based on a true event in 2006 when a group of middle schoolers from Cheongju, South Korea, extorted money from their classmate for about a month, repeatedly beating and burning her using objects in the process.",
      "img": "https://images.chosun.com/resizer/49LbXaVVpnRL2YGnbhKFbWxL-J4=/540x801/smart/cloudfront-ap-northeast-1.images.arcpublishing.com/chosun/HLXDPZC4EDEZHNGFASHIDBVHSI.jpg"
   },
   {
      "id": 4,
      "name": "Celebrity",
      "genres": "Drama, Romantic",
      "creators": "Kim Cheol-kyu, Kim Yi-young",
      "casts": "Park Gyu-young, Kang Min-hyuk, Lee Chung-ah",
      "year": 2023,
      "summary": "Seo Ah-ri (Park Gyu-young) finds herself thrown into a life of fame, wealth, and desire as she explores the world of social media influencers. However, Ah-ri mentions how these influencers buy followers, which tricks laypersons into believing that they are celebrities. As her reputation begins to tarnish during her rise and eventual fall, Ah-ri exposes the scandalous lives of the influencers, involving scams, harassment, drugs, and eventually murder.",
      "img": "https://d2v0j9zp5u17nn.cloudfront.net/wp-content/uploads/2023/05/31131450/celebrity-poster-1.jpeg"
   },
   {
      "id": 5,
      "name": "Mr. Sunshine",
      "genres": "Drama, Romantic, Political, Historic",
      "creators": "Kim Eun-sook, Lee Eung-bok",
      "casts": "Lee Byung-hun, Kim Tae-ri, Yoo Yeon-seok",
      "year": 2018,
      "summary": "Mr. Sunshine centres around Eugene Choi (Lee Byung-hun), who was born into slavery in Joseon. After escaping to the United States at the time of the 1871 Shinmiyangyo, he becomes a Marine Corps officer. When he returns to Joseon for a mission, Eugene meets and falls in love with an aristocrat's granddaughter, Go Ae-shin (Kim Tae-ri), who is part of the Righteous Army. However, their love is challenged by their different classes and the presence of Kim Hui-seong (Byun Yo-han), a nobleman who has been Ae-shin's betrothed since childhood.",
      "img": "https://m.media-amazon.com/images/M/MV5BOWU3MjlmODAtZGU5NS00NmFjLTg1NmItNjU3MjQ5MmM1YWJjXkEyXkFqcGdeQXVyNjc3MjQzNTI@._V1_.jpg"
   },
   {
      "id": 6,
      "name": "Under the Queen's Umbrella",
      "genres": "Drama, Historic",
      "creators": "Kim Hyung-sik, Park Ba-ra",
      "casts": "Kim Hye-soo, Kim Hae-sook, Choi Won-yeong",
      "year": 2022,
      "summary": "Queen Hwa-ryeong (Kim Hye-soo) is expected to embody grace and dignity in her royal role. However, her sons prove to be mischievous troublemakers. Faced with this challenge, the queen decides to abandon strict protocols and embarks on a journey to transform her sons into deserving princes through education and personal growth. With determination and perseverance, she endeavors to instill in her sons the values and skills necessary to fulfill their royal responsibilities, all while navigating the complexities of motherhood and royal life.",
      "img": "https://image.tmdb.org/t/p/original/817aakHe145GTVEi6LzxHSBpbth.jpg"
   },
   {
      "id": 7,
      "name": "Crash Landing on You",
      "genres": "Drama, Romantic, Comedy",
      "creators": "Lee Jung-hyo, Park Ji-eun",
      "casts": "Hyun Bin, Son Ye-jin, Seo Ji-hye",
      "year": 2019,
      "summary": "Yoon Se-ri (Son Ye-jin) is a successful South Korean entrepreneur and a chaebol heiress. One day, while paragliding in Seoul, she is blown off course by a tornado and crash-lands in the North Korean portion of the DMZ. Ri Jeong-hyeok (Hyun Bin), a member of the North Korean elite and a captain in the Korean People's Army is patrolling and discovers Se-ri. He is persuaded to hide her and help her return to the South.",
      "img": "https://m.media-amazon.com/images/M/MV5BMzRiZWUyN2YtNDI4YS00NTg2LTg0OTgtMGI2ZjU4ODQ4Yjk3XkEyXkFqcGdeQXVyNTI5NjIyMw@@._V1_.jpg"
   },
   {
      "id": 8,
      "name": "Sweet Home",
      "genres": "Drama, Horror",
      "creators": "Lee Eung-bok, Hong So-ri, Jang Young-woo",
      "casts": "Song Kang, Lee Jin-uk, Lee Si-young",
      "year": 2020,
      "summary": "After his family died in a vehicular accident, suicidal 18-year-old boy Cha Hyun-soo moves into Room 1410 of an apartment complex called Green Home. He and the people around him start being afflicted with strange symptoms, including malevolent talking voices and nosebleeds. One night, through his video door-phone, he witnesses his girl neighbor from Room 1411 transform into a human-eating monster.",
      "img": "https://m.media-amazon.com/images/M/MV5BNWNjMmQ4MzgtOWY2Ny00MTRhLWI3MmYtOWQ1NWJhMjk4MjQyXkEyXkFqcGdeQXVyNjI4NDY5ODM@._V1_.jpg"
   },
   {
      "id": 9,
      "name": "All of Us Are Dead",
      "genres": "Drama, Horror, Romantic",
      "creators": "Lee JQ, Chun Sung-il, Kim Nam-su",
      "casts": "Park Ji-hu, Yoon Chan-young, Cho Yi-hyun",
      "year": 2022,
      "summary": "In the South Korean city of Hyosan, a deranged science teacher enacts a horrific experiment, causing a local high school to be overrun with zombies. As the outbreak spreads to the city, and the beleaguered authorities struggle to contain it, a group of trapped students must band together and use their wits in order to survive and reach safety.",
      "img": "https://i.namu.wiki/i/q9mOmRVI-GXPhzMykLV_5gLuA9PSMB4i2mwa7bV7exAjOrhhx3WPgGKHK3cyaHthkMwUbsSrBMeXIybPrL-v0A.webp"
   },
   {
      "id": 10,
      "name": "Squid Game",
      "genres": "Drama, Thriller",
      "creators": "Hwang Dong-hyuk",
      "casts": "Lee Jung-jae, Park Hae-soo, Wi Ha-jun",
      "year": 2021,
      "summary": "In a dystopian South Korea, Seong Gi-hun, a divorced father and indebted gambler who lives with his elderly mother, is invited to play a series of children's games for a chance at a large cash prize. Accepting the offer, he is taken to an unknown location where he finds himself among 456 other players who are all in deep financial trouble. The players are made to wear green tracksuits and are kept under watch at all times by masked guards in pink jumpsuits, with the games overseen by the Front Man, who wears a black mask and black uniform.",
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
      updated_data = request.json
      item.update(updated_data)
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




