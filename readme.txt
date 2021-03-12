Requeriments:

Python 3.8
Flask 0.12.2
google-api-core          1.26.0
google-api-python-client 1.12.8
google-auth              1.27.0
google-auth-httplib2     0.0.4
google-auth-oauthlib     0.4.2
googleapis-common-protos 1.53.0

Rodandos os testes localmente: 
  python test_gooogle_contacts_searcher.py


Notas adicionais:
   O projeto foi realizado com a criação de apenas duas classes. Uma delas serve
  exclusivamente para instanciar objetos da classe Contact que por sua vez
  possuem os atributos 'nome' e 'email' que serão utilizados na segunda classe
  GoogleContactsSearcher onde foram criados todos os métodos para a abstração e
  consumo da API ''People'' do Google que foi utilizada para coletar os dados necessários
  do usuário para a finalidade da aplicação: Separar todos os contatos do
  usuário em listas de acordo com seu provedor de e-mail.
   A classe "GoogleContactsSearcher" possue 3 métodos, que foram criados
   pensando na forma mais simples de abstrair a API "People" do google. Ela tem
   como finalidade coletar os contatos do cliente, realizar as tratativas
   necessárias e retornar os valores desejados que serão enviados para o
   front-end. Decidi fazer assim pois acho que é uma maneira simples e
   eficiente de realizar a abstração. 
  

  Abaixo, algumas observações sobre as tecnologias utilizadas:

  -Flask: A utilização do Flask foi excelente visto que a proposta do projeto
  era extremamente simples: Consumir uma API; Abstrair os dados; Retornar os
  dados tratados como informações para o front-end. Visto que esse é um ''Micro
  Framework'', o mesmo exige um baixo nível de complexidade para a
  implementação de um app simples, em comparação com outros Frameworks como
  Django onde seria necessário a realização de diversas configurações iniciais
  e um trabalho de configuração maior na definição de views e registro de apps
  no projeto etc.,

  Unittest: Decidi utilizar o Unittest para a realização dos testes visando a
  objetividade e redução da complexidade. Uma vez que apenas alguns simples
  testes eram necessários, achei melhor evitar utilizar mais dependências para
  fazer algo que poderia facilmente ser feito com uma biblioteca nativa. Apesar
  de outras tecnologias como "Pytest" serem mais difundidas no dia-a-dia, não
  achei que seria necessário a implementação de alguma nesse projeto.

  - Google People API: Uma API extremamente poderosa fornecida pela Google. Com
    ela, podemos obter detalhes sobre os contatos do usuário do app após a
    permissão do mesmo além de ser útil também para o gerenciamento desses
    contatos com funções que não foram abordadas em nosso aplicativo.



