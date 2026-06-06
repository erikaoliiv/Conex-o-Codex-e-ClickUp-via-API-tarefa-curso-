# Registro e Autorizacao de App no Trello com Python

Este repositorio foi criado como entrega de uma tarefa de curso da DIO.  
O objetivo e explicar, de forma simples e pratica, como uma aplicacao Python pode se conectar a uma API externa usando uma chave de acesso, sem expor informacoes sensiveis no codigo.

## Ideia do projeto

Durante meus estudos, percebi que muitos exemplos de autorizacao de aplicativos acabam ficando mais complexos do que precisam ser para um primeiro contato.

Neste projeto, a ideia e mostrar o fluxo essencial:

1. Criar ou registrar um aplicativo na plataforma externa.
2. Gerar uma chave de API ou token de acesso.
3. Guardar essa chave em um arquivo seguro, fora do codigo principal.
4. Ler a chave pelo Python.
5. Fazer uma chamada simples para a API.

Esse mesmo raciocinio foi usado em um caso real de organizacao de tarefas com ClickUp: primeiro conectamos a API, depois criamos uma pasta/arquivo secreto para guardar o token, e entao a automacao passou a consultar e atualizar tarefas conforme as instrucoes dadas.

## Relacao com Trello

No Trello, o processo segue a mesma logica:

- o usuario gera uma chave de API;
- autoriza o acesso da aplicacao;
- guarda o token com seguranca;
- o Python usa essas credenciais para acessar quadros, listas e cards.

Este repositorio nao contem chaves reais. Os arquivos mostram apenas exemplos seguros.

## Estrutura do projeto

```text
.
|-- README.md
|-- main.py
|-- .env.example
|-- .gitignore
`-- requirements.txt
```

## Como configurar

1. Clone o repositorio:

```bash
git clone https://github.com/seu-usuario/dio-trello-python-api.git
cd dio-trello-python-api
```

2. Crie um ambiente virtual:

```bash
python -m venv .venv
```

3. Ative o ambiente virtual:

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

4. Instale as dependencias:

```bash
pip install -r requirements.txt
```

5. Copie o arquivo de exemplo:

```bash
copy .env.example .env
```

No Linux/macOS:

```bash
cp .env.example .env
```

6. Preencha o arquivo `.env` com suas credenciais reais:

```env
TRELLO_API_KEY=sua_chave_aqui
TRELLO_TOKEN=seu_token_aqui
```

## Por que usar `.env`?

O arquivo `.env` guarda informacoes sensiveis, como tokens e chaves de API.  
Ele nao deve ser enviado para o GitHub.

Por isso, este projeto inclui:

- `.env.example`: modelo seguro, pode ir para o GitHub;
- `.env`: arquivo real com segredos, fica somente no computador;
- `.gitignore`: impede que o `.env` seja enviado por engano.

## Exemplo de uso

O arquivo `main.py` le as variaveis de ambiente e mostra como uma chamada para a API poderia ser feita.

```bash
python main.py
```

Se as variaveis estiverem configuradas, o script mostra que as credenciais foram carregadas com seguranca.

## Boas praticas

- Nunca publicar tokens ou chaves reais no GitHub.
- Usar `.env` ou variaveis de ambiente.
- Manter um `.env.example` para orientar outras pessoas.
- Revogar e gerar uma nova chave caso algum segredo seja exposto.
- Separar configuracao sensivel do codigo principal.

## Conclusao

Este projeto mostra que a autorizacao de uma aplicacao nao precisa ser complicada no inicio.  
O ponto mais importante e entender o fluxo:

**gerar credenciais, guardar com seguranca e usar no Python somente quando necessario.**

Essa logica pode ser aplicada ao Trello, ClickUp e outras APIs usadas em projetos reais.
