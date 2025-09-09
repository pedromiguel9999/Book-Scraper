import requests
from bs4 import BeautifulSoup
import csv

# URL da primeira página do site Books to Scrape
url = "http://books.toscrape.com/catalogue/page-1.html"

# Fazer requisição HTTP
response = requests.get(url)
if response.status_code != 200:
    print("Erro ao acessar o site")
    exit()

# Parse do HTML com BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Encontrar todos os livros na página
# Cada livro está dentro de uma <article> com classe "product_pod"
livros = soup.find_all("article", class_="product_pod")

# Lista para armazenar dados
dados_livros = []

for livro in livros:
    # Título do livro
    titulo = livro.h3.a["title"]
    
    # Preço do livro
    preco = livro.find("p", class_="price_color").get_text(strip=True)
    
    # Disponibilidade
    disponibilidade = livro.find("p", class_="instock availability").get_text(strip=True)
    
    dados_livros.append([titulo, preco, disponibilidade])

# Exibir resultados no terminal
for i, (titulo, preco, disponibilidade) in enumerate(dados_livros, 1):
    print(f"{i}. {titulo} | {preco} | {disponibilidade}")

# Salvar em CSV
with open("livros.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Título", "Preço", "Disponibilidade"])
    writer.writerows(dados_livros)

print("\nDados salvos em livros.csv")
