#Aiden Clarke 
#11/19/23
#dad joke 
import requests
import random 
'''
url = "https://icanhazdadjoke.com/j"
headers = {"Accept": "application/json"}
response = requests.get(url, headers= headers)

json_data = response.json()
'''

#function to get the data from api

def get_r_joke():
    #get data 
    url = "https://icanhazdadjoke.com/"
    headers = {"Accept": "application/json"}
#actually get data
    response = requests.get(url , headers=headers) 

    if response.status_code == 200 :
        joke_data=response.json()
        return joke_data['joke']
    else: #incase of failure v
            return "failed to fetch dad joke"

def main():
    #maybe a number of jokes option in main
    jokenumbeer = 5

#print out the number of jokes with a counter
    for n in range(jokenumbeer):
        joke= get_r_joke()
        print("DAD JOKE NUMBER ",n+1," IS \n",joke)

main()


