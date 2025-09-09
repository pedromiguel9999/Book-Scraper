

##Breve Descrição 

Este projeto consiste em um **web scraper** para o site [Books to Scrape](http://books.toscrape.com/), com o objetivo de extrair informações sobre livros de forma automatizada.  
O scraper coleta os dados principais de cada livro e salva em um arquivo CSV, permitindo análises e consultas futuras.

---

## Funcionalidades

- Extrai o **título** de cada livro.
- Extrai o **preço** de cada livro.
- Extrai a **disponibilidade em estoque** de cada livro.
- Salva todos os dados em um arquivo **CSV** (`livros.csv`).
- Exibe os resultados no terminal.
- 
## Tec Utilizadas

- **Python 3**  
- **Requests** – para fazer requisições HTTP.  
- **BeautifulSoup (bs4)** – para processar e navegar pelo HTML.  
- **CSV** – para salvar os dados de forma estruturada.  

---

## Estrutura do Código

1. **Requisição HTTP**  
   O script acessa a página do site usando `requests.get(url)`.

2. **Parse do HTML**  
   O conteúdo da página é processado pelo `BeautifulSoup` para buscar elementos HTML específicos.

3. **Extração dos Dados**  
   Cada livro está dentro de um `<article>` com a classe `product_pod`.  
   - **Título**: obtido pelo atributo `title` da tag `<a>` dentro do `<h3>`.  
   - **Preço**: contido na `<p>` com classe `price_color`.  
   - **Disponibilidade**: contida na `<p>` com classe `instock availability`.  

4. Armazenamento em CSV
   Os dados são salvos em `livros.csv` usando o módulo `csv` do Python.

---

## Resultado Estimado

- Um arquivo CSV (`livros.csv`) com o seguinte formato:

| Título                           | Preço   | Disponibilidade |
|---------------------------------|---------|----------------|
| A Light in the Attic             | £51.77  | In stock       |
| Tipping the Velvet               | £53.74  | In stock       |
| Soumission                       | £50.10  | In stock       |

- Impressão no terminal de todos os livros extraídos.

---

## Como Executar

1. Clone este repositório:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd books_scraper
