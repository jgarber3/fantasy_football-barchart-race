import pandas
import requests
import json

#TEAMS_URL = "http://api/myfantasyleague.com/2023/export?TYPE=

def get_data_from_api(url):
        response = requests.get(url)

        if response.status_code == 200:
             data = response.json()
             return data
        else:
             print("Error occurred while fetching data from API.")
             return None


def get_team_names():
    response = get_data_from_api(TEAMS_URL)
    if response:

        local_dict = {}

        league_dict = response["league"]
        team_dict = league_dict["franchises"]
        team_list = team_dict["franchise"]

        for x in team_list:
            local_dict[x["id"]] = x["name"]

        if local_dict:
            return local_dict
        else:
            return None


TEAMS_URL = "http://api.myfantasyleague.com/2022/export?TYPE=league&L=30532&JSON=1"

teams = get_team_names()
#print(teams)



source_params = [ ['2000','67640'] , ['2001','77147'], ['2002','72584'],['2003','61156'],['2004','56991'],['2005','62719'],['2006','74602'],['2007','50645'],['2008','60607'],['2009','70874'],['2010','57806'],['2011','31632'],['2012','11278'],['2013','12818'],['2014','28756'],['2015','49827'],['2016','30532'],['2017','30532'],['2018','30532'],['2019','30532'],['2020','30532'],['2021','30532'],['2022','30532']]

dataset =  []

for count, source_index in enumerate(source_params):
    print("Year: " + source_index[0])
    #print("counter is " + str(count))
    year = {}
    api = get_data_from_api("https://api.myfantasyleague.com/" + source_index[0] + "/export?TYPE=standings&L=" + source_index[1] + "&W=14&JSON=1")
    if api:
        year["year"] = source_index[0]

        league_dict = api["leagueStandings"]
        team_list = league_dict["franchise"]
        for x in team_list:
            team_id = x["id"]
            points = x["pf"]
            if(count == 0):
                year[teams[team_id]] = points
            else:
                total = int(dataset[count-1][teams[team_id]])
                year[teams[team_id]] = str(int(dataset[count-1][teams[team_id]]) + int(points))

        dataset.insert(count,year)

df = pandas.DataFrame(dataset)
df = df.set_index("year");


print(df)
df.to_excel('./data.xlsx')



