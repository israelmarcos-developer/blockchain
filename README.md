Blockchain com Flask :lock::link::moneybag:
Este é um exemplo simples de implementação de uma blockchain em Python com o framework Flask.

Requisitos :clipboard:
Python 3
Flask (pip install flask)
Como executar :rocket:
Clone o repositório ou baixe o arquivo blockchain.py
Abra um terminal na pasta raiz do projeto
Execute python blockchain.py
Os endpoints estarão disponíveis em http://localhost:5000
Como funciona :gear:
A classe Blockchain implementa a lógica da blockchain, incluindo a criação de blocos, mineração, validação e geração de hashes.

A classe Flask é utilizada para expor endpoints que permitem a interação com a blockchain, incluindo mineração de novos blocos, obtenção da cadeia de blocos completa e verificação da validade da cadeia.

Endpoints :computer:
GET /mine_block: realiza a mineração de um novo bloco e adiciona à cadeia.
GET /get_chain: retorna a cadeia completa de blocos.
GET /is_valid: verifica se a cadeia de blocos é válida.
Licença :scroll:
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais informações.