import requests
import json
map_id = ["520163", "520247", "517385", "511498", "531963", "529093", "446433", "406385", "515782", "226550", "38016", "354669", "70185", "100024", "114296"]
map_scores = []
map_max_scores = []
map_details_list = []

def has_error_message(json_data):
        if isinstance(json_data, dict):
            return "errorMessage" in json_data and json_data["errorMessage"] == "No scores found"
        return False

for map in map_id:
    response = requests.get(f'https://scoresaber.com/api/leaderboard/by-id/' + map + '/scores?countries=it&page=1')
    pizzi = requests.get(f"https://scoresaber.com/api/leaderboard/by-id/" + map + "/scores?countries=us&search=sionpizzi")
    map_details = requests.get(f"https://scoresaber.com/api/leaderboard/by-id/" + map + "/info")
    if response.status_code == 200:
        scores_dict = response.json()
        pizzi_dict = pizzi.json()
        scores = scores_dict['scores'][:10]
        map_scores.append(scores)
        map_json = map_details.json()
        map_details_list.append(map_json)
        map_max_scores.append(map_json["maxScore"])
        if has_error_message(pizzi_dict) == True:
            print("pizzi non trovato:nerd:")
        else:
            pizziscore = pizzi_dict["scores"][:1]
            scores.extend(pizziscore)
            print("pizzi trovato:tf:")

        #print(scores_dict) # godo
        #print(scores)
        print("scrivo " + map + ".json")
        with open(map + '.json', 'w', encoding="utf-16") as f:
            json.dump(scores, f, indent=2)
            print(map + ".json scritto")
            scores.sort(key=lambda score: score['baseScore'], reverse=True)

html = '<html>\n'
html += '<head>\n'
html += '<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">\n'
html += "<title>BSEUC Qualifiers Italia</title>\n"
html += "<style>\n"
html += "   table, th, td {\n"
html += "   border: 2px solid black;\n"
html += "   text-align: center;\n"
html += "   }\n"
html += "   table, p {\n"
html += "   display: none;\n"
html += "   }\n"
html += "   h1, h2, h3{\n"
html += "   text-align: center;\n"
html += "   }\n"
html += "   .center {\n"
html += "   margin-left: auto;\n"
html += "   margin-right: auto;\n"
html += "   }\n"
html += "</style>\n"
html += '</head>\n'
html += '<body>\n'
html += "<div>\n"
html += '  <button type="button" onclick="selectAcc()">Accuracy</button>\n'
html += '  <button type="button" onclick="selectSpeed()">Speed</button>\n'
html += '  <button type="button" onclick="selectTech()">Tech</button>\n'
html += '  <button type="button" onclick="selectJoker()">Joker</button>\n'
html += '  <button type="button" onclick="selectHist()">Historical</button>\n'
html += '</div>'
html += '<script> function selectAcc() { \n'
html += '    const tables = document.getElementsByClassName("table");\n' 
html += '    console.log(tables); for(var i = 0; i < tables.length; i++){\n' 
html += '        tables[i].style.display = "none"};\n'
html += '    const selected = document.getElementsByClassName("category0");\n' 
html += '    for(var i = 0; i < selected.length; i++){\n' 
html += '        selected[i].style.display = "table";\n'
html += '        }}</script>\n'
html += '<script> function selectSpeed() { \n'
html += '    const tables = document.getElementsByClassName("table");\n' 
html += '    console.log(tables); for(var i = 0; i < tables.length; i++){\n' 
html += '        tables[i].style.display = "none"};\n'
html += '    const selected = document.getElementsByClassName("category1");\n' 
html += '    for(var i = 0; i < selected.length; i++){\n' 
html += '        selected[i].style.display = "table";\n'
html += '        }}</script>\n'
html += '<script> function selectTech() { \n'
html += '    const tables = document.getElementsByClassName("table");\n' 
html += '    console.log(tables); for(var i = 0; i < tables.length; i++){\n' 
html += '        tables[i].style.display = "none"};\n'
html += '    const selected = document.getElementsByClassName("category2");\n' 
html += '    for(var i = 0; i < selected.length; i++){\n' 
html += '        selected[i].style.display = "table";\n'
html += '        }}</script>\n'
html += '<script> function selectJoker() { \n'
html += '    const tables = document.getElementsByClassName("table");\n' 
html += '    console.log(tables); for(var i = 0; i < tables.length; i++){\n' 
html += '        tables[i].style.display = "none"};\n'
html += '    const selected = document.getElementsByClassName("category3");\n' 
html += '    for(var i = 0; i < selected.length; i++){\n' 
html += '        selected[i].style.display = "table";\n'
html += '        }}</script>\n'
html += '<script> function selectHist() { \n'
html += '    const tables = document.getElementsByClassName("table");\n' 
html += '    console.log(tables); for(var i = 0; i < tables.length; i++){\n' 
html += '        tables[i].style.display = "none"};\n'
html += '    const selected = document.getElementsByClassName("category4");\n' 
html += '    for(var i = 0; i < selected.length; i++){\n' 
html += '        selected[i].style.display = "table";\n'
html += '        }}</script>\n'
for score in map_scores:
    max_score = map_max_scores[map_scores.index(score)]
    category = (map_scores.index(score)) // 3
    html += f'<table class="table category{category}">\n'
    html += '  <thead>\n'
    html += f'      <p class="table category{category}">\n'
    html += f'        {map_details_list[map_scores.index(score)]["songName"]} - {map_details_list[map_scores.index(score)]["songAuthorName"]}\n'
    html += '      </p>\n'
    html += '    <tr>\n'
    html += '      <th scope="col">#</th>\n'
    html += '      <th scope="col">Name</th>\n'
    html += '      <th scope="col">Score</th>\n'
    html += '      <th scope="col">Miss</th>\n'
    html += '      <th scope="col">Punti</th>\n'
    html += '    </tr>\n'
    html += '  </thead>\n'
    html += '  <tbody>\n'
    for i, item in enumerate(score):
        row_class = ""
        if i < 3:
            row_class = "table-success"
        elif i == 3:
            row_class = "alert-warning"
        else:
            row_class = "table-danger"
        points = 1
        if i < 3:
            points = 1000
        elif i == 3:
            points = 100
        elif i == 4:
            points = 10
        elif i == 5:
            points = 1
        perc = format((item["baseScore"] / max_score) * 100, ".2f")
        miss = item["badCuts"] + item["missedNotes"]
        html += f'    <tr class="{row_class}">\n'
        html += f'      <th scope="row">{i + 1}</th>\n'
        html += f'      <td>{item["leaderboardPlayerInfo"]["name"]}</td>\n'
        html += f'      <td>{perc}%</td>\n'
        html += f'      <td>{miss}</td>\n'
        html += f'      <td>{points}</td>\n'
        html += '    </tr>\n'

html += '  </tbody>\n'
html += '</table>\n'
html += '</body>\n'
with open("index.html", "w", encoding="utf-16") as f:
    f.write(html)
    print("index.html scritto")