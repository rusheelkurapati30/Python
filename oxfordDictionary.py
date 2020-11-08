# Program on oxford dictionary to print the meaning of the given word.

import requests
app_id = "cd9f1a0d"
app_key = "1f766ec01c258b21809ed532ff88579f"
language = "en-gb"
word_id = input("\nPlease enter a word: ")
url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
response = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
print(type(response))
if response:
    definitionData = eval(response.text)
    print(type(definitionData))
    definitionList = []
    for result in definitionData['results'][0]["lexicalEntries"][0]["entries"][0]['senses']:
    	definitionList.append(result['definitions'][0])
    # print(definitionList)
    print("\nThe list of meanings available for " + word_id + " is: \n")
    counter = 0
    for definition in definitionList:
    	counter += 1
    	print(str(counter) + ". " + definition)
else:
    print("\nNo matches found please try again with different word")




































    # for result in definitionData['results']:
    # 	for lexicalEntry in result['lexicalEntries']:
    # 		for entry in lexicalEntry['entries']:
    # 			for sense in entry['senses']:
# definitions = []
# for definition in wordMeaning["results"][0]["lexicalEntries"][0]["entries"][0]["senses"]:
# 	definition.append(sense["definitions"][0]
# x = wordMeaning["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"][0]
# y = wordMeaning["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["subsenses"][0]["definitions"][0]