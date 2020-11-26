# exibindo os dados obtidos
import requests

base_url = "https://scrapethissite.com/pages/advanced/?gotcha=headers"

response = requests.get(base_url, headers={
  "Accept": "application/json;text/html,application/xhtml+xml,application/xml;"
  "q=0.9,image/webp,image/apng,*/*;"
  "q=0.8,application/signed-exchange;v=b3;q=0.9",
  "Accept-Language":	"pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
  "User-Agent":	"Mozilla/5.0 (X11; Linux x86_64)"
  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
})
assert "bot detected" not in response.text

# conteudo recebido da requisicao
print(response.text)
