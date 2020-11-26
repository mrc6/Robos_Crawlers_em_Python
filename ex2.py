# exibindo os dados obtidos
import requests
import json

response = requests.get("https://api.github.com/users")
giti_users = json.loads(response.text)
users = []

# conteudo recebido da requisicao
# print(response.text)

# imprimindo usuarios e url
for items in giti_users:
    login = items["login"]
    url = items["url"]
    users.append({"login": login, "url": url})
    print(login, url)

# print(users)
