# 📊 PokéDados

Terminei a cadeira de **Modelagem de Dados** no meu curso de **Cibersegurança** e deu aquela vontade de colocar a mão na massa e aplicar o que aprendi num projeto do zero. Foi assim que surgiu o **PokéDados**! 

A ideia foi criar um fluxo completo: desde consumir uma API externa até modelar o banco de dados em MySQL, gerar a massa de dados e criar uma interface visual interativa pra ver tudo a funcionar.

---

### 🚀 O que fiz na prática

* **Consumo de API:** Criei um script em Python (`requests`) que consome dados diretos da **PokéAPI** (nome, atributos base, tipos, etc.).
* **Modelagem de Banco (MySQL):** Estruturei o banco relacional do zero (`01_schema.sql`) com tabelas para espécies, tipos, treinadores e capturas, garantindo integridade referencial.
* **Automação de Dados:** Criei o script `gerar_dados.py` para popular o banco automaticamente (`02_dados.sql`) sem quebrar chaves primárias e estrangeiras.
* **Consultas SQL Analíticas:** Escrevi queries avançadas (`03_consultas.sql`) usando `JOIN`, `GROUP BY`, funções de agregação e subqueries para extrair relatórios sobre os Pokémon e treinadores.
* **Front-end / Dashboard:** Desenvolvi um dashboard interativo em HTML, CSS e JavaScript com design *Glassmorphism* para explorar a Pokédex, estatísticas e consultas do banco.

---

### 🛠️ Tecnologias Utilizadas

* **Linguagens:** Python, SQL, HTML5, CSS3, JavaScript
* **Banco de Dados:** MySQL / MySQL Workbench
* **Ferramentas:** VS Code, Git, GitHub Pages, PokéAPI

---

### 📁 Estrutura do Repositório

```text
pokedados/
├── index.html        # Interface Web (Dashboard)
├── gerar_dados.py    # Script Python para consumir PokéAPI e gerar SQL
├── sql/
│   ├── 01_schema.sql    # Criação das tabelas e relacionamentos
│   ├── 02_dados.sql     # Povoamento da base de dados
│   └── 03_consultas.sql # Queries analíticas e relatórios
└── README.md
