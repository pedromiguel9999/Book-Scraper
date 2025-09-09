import requests
from bs4 import BeautifulSoup
import csv


url = "http://books.toscrape.com/catalogue/page-1.html"


response = requests.get(url)
if response.status_code != 200:
    print("Erro ao acessar o site")
    exit()

soup = BeautifulSoup(response.text, "html.parser")

livros = soup.find_all("article", class_="product_pod")


dados_livros = []

for livro in livros:
    
    titulo = livro.h3.a["title"]
    
    
    preco = livro.find("p", class_="price_color").get_text(strip=True)
    
    
    disponibilidade = livro.find("p", class_="instock availability").get_text(strip=True)
    
    dados_livros.append([titulo, preco, disponibilidade])


for i, (titulo, preco, disponibilidade) in enumerate(dados_livros, 1):
    print(f"{i}. {titulo} | {preco} | {disponibilidade}")

with open("livros.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Título", "Preço", "Disponibilidade"])
    writer.writerows(dados_livros)

print("\nDados salvos em livros.csv")
