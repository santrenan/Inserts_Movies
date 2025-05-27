Instruções para criar a tabela `movies_data` no banco de dados MySQL. Essa tabela é destinada a armazenar informações sobre filmes, como nome, data de lançamento, ano, URI e status.


Crie a tabela no seu banco MySQL com o seguinte comando:

```sql
CREATE TABLE `movies_data` (
   `movie_id` int NOT NULL AUTO_INCREMENT,
   `date` date DEFAULT NULL,
   `name` varchar(100) DEFAULT NULL,
   `year` year DEFAULT NULL,
   `uri` varchar(255) DEFAULT NULL,
   `status` enum('not_watched','watched') DEFAULT 'not_watched',
   PRIMARY KEY (`movie_id`)
 );

```
