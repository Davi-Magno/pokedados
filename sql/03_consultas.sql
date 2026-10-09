USE pokedados;

-- 1. Top 5 Pokémon com maior base de ataque
SELECT 
    numeroPokedex,
    nome,
    ataqueBase,
    hpBase
FROM especies
ORDER BY ataqueBase DESC
LIMIT 5;

-- 2. Quantidade total de Pokémon capturados por cada treinador
SELECT 
    t.nome AS treinador,
    t.cidadeOrigem,
    COUNT(c.capturaID) AS total_capturas
FROM treinadores t
LEFT JOIN capturas c ON t.treinadorID = c.Treinadores_treinadorID
GROUP BY t.treinadorID, t.nome, t.cidadeOrigem
ORDER BY total_capturas DESC;

-- 3. Média de nível dos Pokémon capturados por espécie
SELECT 
    e.nome AS especie,
    ROUND(AVG(c.nivel), 1) AS media_nivel,
    COUNT(c.capturaID) AS quantidade_capturada
FROM especies e
JOIN capturas c ON e.especieID = c.especies_especieID
GROUP BY e.especieID, e.nome
ORDER BY media_nivel DESC;

-- 4. Lista de Pokémon com os seus respetivos tipos (Concatenação de tipos)
SELECT 
    e.numeroPokedex,
    e.nome AS pokemon,
    GROUP_CONCAT(tp.nome SEPARATOR ', ') AS tipos
FROM especies e
JOIN tipos_has_especies te ON e.especieID = te.especies_especieID
JOIN tipos tp ON te.tipos_tipoID = tp.tipoID
GROUP BY e.especieID, e.numeroPokedex, e.nome
ORDER BY e.numeroPokedex ASC;

-- 5. Treinador que capturou o Pokémon de maior nível
SELECT 
    t.nome AS treinador,
    e.nome AS pokemon,
    c.apelido,
    c.nivel,
    c.dataCaptura
FROM capturas c
JOIN treinadores t ON c.Treinadores_treinadorID = t.treinadorID
JOIN especies e ON c.especies_especieID = e.especieID
WHERE c.nivel = (SELECT MAX(nivel) FROM capturas);