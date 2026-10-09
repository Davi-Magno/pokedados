import random
import requests
from datetime import datetime, timedelta

# Garantir reprodutibilidade nos dados aleatórios
random.seed(42)

TOTAL_POKEMON = 40

NOMES_TREINADORES = ["Davi", "Ash", "Brock", "Serena", "Lucas Aprigio", "Mariana", "Sanalu"]  
CIDADES_PE = ["Recife", "Olinda", "Caruaru", "Petrolina", "Garanhuns", "Jaboatao dos Guararapes", "Sao Lourenco da Mata"]

def buscar_dados_pokeapi():
    print("A procurar dados na PokéAPI...")
    especies = []
    especies_tipos = []
    tipos_set = set()

    for i in range(1, TOTAL_POKEMON + 1):
        url = f"https://pokeapi.co/api/v2/pokemon/{i}"
        res = requests.get(url)

        if res.status_code == 200:
            data = res.json()

            numero = data['id']
            nome = data['name'].capitalize()
            geracao = 1

            stats = {s['stat']['name']: s['base_stat'] for s in data['stats']}
            hp = stats.get('hp', 0)
            ataque = stats.get('attack', 0)
            defesa = stats.get('defense', 0)
            velocidade = stats.get('speed', 0)

            especies.append((numero, nome, geracao, hp, ataque, defesa, velocidade))

            for t in data['types']:
                nome_tipo = t['type']['name'].capitalize()
                tipos_set.add(nome_tipo)
                especies_tipos.append((numero, nome_tipo))

    return list(tipos_set), especies, especies_tipos

def gerar_sql():
    tipos, especies, especies_tipos = buscar_dados_pokeapi()
    
    sql_lines = [
        "SET FOREIGN_KEY_CHECKS = 0;\n",
        "USE pokedados;\n\n"
    ]
    
    sql_lines.append("-- 1. Inserir Tipos\n")
    sql_lines.append("INSERT INTO tipos (tipoID, nome) VALUES\n")
    tipos_sorted = sorted(tipos)
    sql_lines.append(",\n".join([f"({idx + 1}, '{t}')" for idx, t in enumerate(tipos_sorted)]) + ";\n\n")
    
    tipo_to_id = {nome: idx + 1 for idx, nome in enumerate(tipos_sorted)}
    
    sql_lines.append("-- 2. Inserir Especies\n")
    sql_lines.append("INSERT INTO especies (numeroPokedex, nome, geracao, hpBase, ataqueBase, defesaBase, velocidadeBase) VALUES\n")
    sql_lines.append(",\n".join([f"({e[0]}, '{e[1]}', {e[2]}, {e[3]}, {e[4]}, {e[5]}, {e[6]})" for e in especies]) + ";\n\n")
    
    sql_lines.append("-- 3. Inserir Treinadores\n")
    sql_lines.append("INSERT INTO treinadores (nome, cidadeOrigem) VALUES\n")
    sql_lines.append(",\n".join([f"('{nome}', '{random.choice(CIDADES_PE)}')" for nome in NOMES_TREINADORES]) + ";\n\n")
    
    sql_lines.append("-- 4. Inserir Tipos x Especies\n")
    sql_lines.append("INSERT INTO tipos_has_especies (tipos_tipoID, especies_especieID) VALUES\n")
    rel_values = [f"({tipo_to_id[nome_tipo]}, {num_pokedex})" for num_pokedex, nome_tipo in especies_tipos]
    sql_lines.append(",\n".join(rel_values) + ";\n\n")
    
    sql_lines.append("-- 5. Inserir Capturas\n")
    sql_lines.append("INSERT INTO capturas (apelido, nivel, dataCaptura, Treinadores_treinadorID, especies_especieID) VALUES\n")
    
    capturas_values = []
    data_inicial = datetime(2024, 1, 1)
    apelidos = ["Trovoada", "Feroz", "Fofinho", "Valente", "Sombra", "Faisca", "Tita", "Soneca", "Bolinha"]
    
    for _ in range(60):
        apelido = random.choice(apelidos)
        nivel = random.randint(5, 100)
        data_cap = (data_inicial + timedelta(days=random.randint(0, 300))).strftime('%Y-%m-%d')
        treinador_id = random.randint(1, len(NOMES_TREINADORES))
        especie_id = random.randint(1, len(especies))
        capturas_values.append(f"('{apelido}', {nivel}, '{data_cap}', {treinador_id}, {especie_id})")
        
    sql_lines.append(",\n".join(capturas_values) + ";\n\n")
    sql_lines.append("SET FOREIGN_KEY_CHECKS = 1;\n")
    
    with open("sql/02_dados.sql", "w", encoding="utf-8") as f:
        f.writelines(sql_lines)
        
    print("Sucesso! O ficheiro 'sql/02_dados.sql' foi gerado.")

if __name__ == "__main__":
    gerar_sql()