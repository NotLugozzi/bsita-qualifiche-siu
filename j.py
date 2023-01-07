import requests
import json
from jinja2 import Template
map_id = "280304" #todo: nome mappa da id -o- lista nomi mappe
response = requests.get(f'https://api.codetabs.com/v1/proxy?quest=https://scoresaber.com/api/leaderboard/by-id/{map_id}/scores?countries=it&page=1')
# pizzi = requests.get(f"https://api.codetabs.com/v1/proxy?quest=https://scoresaber.com/api/leaderboard/by-id/{map_id}/scores?countries=us&search=sionpizzi")
if response.status_code == 200:
    scores_dict = response.json()
    # print(scores_dict) godo
    scores = scores_dict['scores'][:10]
    with open('scores.json', 'w', encoding="utf-16") as f:
     json.dump(scores, f)
    scores.sort(key=lambda score: score['baseScore'], reverse=False)
    template = Template("""
    <html>
    <head>
        <title>zio pera</title>
        <style>
           table, th, td {
           border: 2px solid black;
           text-align: center;
           }
           h1{
           text-align: center;
           }
           .center {
            margin-left: auto;
            margin-right: auto;
            }
        </style>
    </head>
    <body>
        <h1>punteggio del godo</h1>
        <table class="center">
        <tr>
            <th style="padding:10px">Player</th>
            <th style="padding:10px">Score</th>
            <th style="padding:10px">FC</th>
            <th style="padding:10px">Last Played Date</th>
        </tr>
        {% for score in scores %}
           <tr>
            <td>{{ score.leaderboardPlayerInfo.name }}</td>
            <td>{{ score.baseScore }}</td>
            <td>{{ score.fullCombo }}</td>
            <td>{{ score.timeSet }}</td>
          </tr>
          {% endfor %}
        </table>
      </body>
    </html>
    """)
    html = template.render(scores=scores)
    with open("index.html", "w", encoding="utf-16") as f:
     f.write(html)
    with open('scores.json', 'w') as f:
     json.dump(scores, f)    
else:
    print("An error occurred:", response.status_code)