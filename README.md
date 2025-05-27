# Instruções para Criar a Tabela `movies_data` no MySQL

Esta documentação explica como criar a tabela `movies_data` no banco de dados MySQL. A tabela será usada para armazenar informações sobre filmes, como nome, data de lançamento, ano, URI e status.

## Criar a Tabela no MySQL

Para criar a tabela no seu banco MySQL, execute o seguinte comando:

```sql
CREATE TABLE `movies_data` (
   `movie_id` int NOT NULL AUTO_INCREMENT,
   `date` date DEFAULT NULL,
   `name` varchar(100) DEFAULT NULL,
   `year` year DEFAULT NULL,
   `uri` varchar(255) DEFAULT NULL,
   `status` enum('not_watched','watched') DEFAULT 'not_watched',
   PRIMARY KEY (`movie_id`),
   UNIQUE KEY `unique_name_year` (`name`, `year`)
);
```

### Descrição dos Campos:

- **movie_id**: Identificador único para cada filme (chave primária), auto-incrementado.
- **date**: Data em que o filme foi assistido ou adicionado à lista.
- **name**: Nome do filme.
- **year**: Ano de lançamento do filme.
- **uri**: URI do filme no Letterboxd.
- **status**: O status do filme, pode ser `'not_watched'` ou `'watched'`. O valor padrão é `'not_watched'`.

---

## Obtendo o Arquivo `movies_list.csv` no Letterboxd

O arquivo `movies_list.csv` contém informações sobre os filmes que você assistiu ou deseja adicionar ao seu banco de dados. Para obter esse arquivo, siga as etapas abaixo:

### Passo 1: Acesse o Letterboxd
Vá até [Letterboxd](https://letterboxd.com) e faça login na sua conta.

### Passo 2: Vá para sua Lista de Filmes
Acesse sua lista de filmes, como a lista de "Filmes assistidos" ou uma lista personalizada que você tenha criado.

### Passo 3: Exporte sua Lista
No Letterboxd, há uma opção para exportar sua lista para o formato CSV. Normalmente, você pode encontrar essa opção no menu de configurações da lista.

### Passo 4: Exporte o arquivo como `movies_list.csv`
Exporte a lista para um arquivo CSV com o nome `movies_list.csv`. Este arquivo conterá as seguintes colunas para cada filme:

- **Date**: Data em que o filme foi assistido ou adicionado.
- **Name**: Nome do filme.
- **Year**: Ano de lançamento.
- **Letterboxd_URI**: O link do filme no Letterboxd.
