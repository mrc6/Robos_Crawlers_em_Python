# exibindo os dados obtidos
import requests

response = requests.get("https://httpbin.org/encoding/utf8")

# conteudo recebido da requisicao
print(response.text)
