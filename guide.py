from wit import Wit 

access_token = "" #Insert token
client = Wit(access_token = access_token) #Input access token for Wit API

message_text = input("Ask a message: " ) #Type in question for Fall 2024 courses at UNCC

resp = client.message(message_text) #Natural language processing through Wit API
print(resp)
entity = respentity = list(resp['entities'])[0] 
value = resp['entities'][entity][0]['value']
print(value) #Intended Response is given

#This project is licensed under the MIT License.

