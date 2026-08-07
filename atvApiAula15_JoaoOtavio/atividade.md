Windows PowerShell
Copyright (C) Microsoft Corporation. Todos os direitos reservados.















PS H:\python\2-etapa\Aula15-API> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>> >>   -Method POST `
>> >>   -ContentType "application/json" `
>> >>   -Body '{"titulo":"NOME DO LIVRO","autor":"NOME DO AUTOR","ano": 1945}'
No linha:3 caractere:1
+ >>   -ContentType "application/json" `
+ ~~~~~~~~~~~~~~~~~
O fluxo de saída deste comando já foi redirecionado.
No linha:4 caractere:1
+ >>   -Body '{"titulo":"NOME DO LIVRO","autor":"NOME DO AUTOR","ano":  ...
+ ~~~~~~~~~~
O fluxo de saída deste comando já foi redirecionado.
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : StreamAlreadyRedirected
 
PS H:\python\2-etapa\Aula15-API> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"NOME DO LIVRO","autor":"NOME DO AUTOR","ano": 1945}'
Invoke-RestMethod : Impossível conectar-se ao servidor remoto
No linha:1 caractere:1
+ Invoke-RestMethod http://127.0.0.1:5000/api/livros `
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (:) [Invoke-RestMethod], WebException
    + FullyQualifiedErrorId : System.Net.WebException,Microsoft.PowerShell.Commands.InvokeRestMethodCommand
 
PS H:\python\2-etapa\Aula15-API> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"NOME DO LIVRO","autor":"NOME DO AUTOR","ano":1945}'
Invoke-RestMethod : Impossível conectar-se ao servidor remoto
No linha:1 caractere:1
+ Invoke-RestMethod http://127.0.0.1:5000/api/livros `
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (:) [Invoke-RestMethod], WebException
    + FullyQualifiedErrorId : System.Net.WebException,Microsoft.PowerShell.Commands.InvokeRestMethodCommand
 
PS H:\python\2-etapa\Aula15-API> ^C
PS H:\python\2-etapa\Aula15-API> Invoke-RestMethod http://127.0.0.1:5000/api/livros -Method POST -ContentType "application/json" -Body '{"titulo":"NOME DO LIVRO","autor":"NOME DO AUTOR","ano":1945}'
>>
Invoke-RestMethod : Impossível conectar-se ao servidor remoto                 
No linha:1 caractere:1
+ Invoke-RestMethod http://127.0.0.1:5000/api/livros -Method POST -Cont ...
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (:) [Invoke-RestMethod], WebException
    + FullyQualifiedErrorId : System.Net.WebException,Microsoft.PowerShell.Commands.InvokeRestMethodCommand
 
PS H:\python\2-etapa\Aula15-API> Invoke-RestMethod http://127.0.0.1:5000/api/livros -Method POST -ContentType "application/json" -Body '{"titulo":"NOME DO LIVRO","autor":"NOME DO AUTOR","ano":1945}'
>>


ano          : 1945
autor        : NOME DO AUTOR
data_criacao : 2026-07-31 10:42:24.220233
id           : 4
titulo       : NOME DO LIVRO



PS H:\python\2-etapa\Aula15-API> Invoke-RestMethod http://127.0.0.1:5000/api/livros -Method POST -ContentType "application/json" -Body '{"titulo":"NOME DO LIVRO","autor":"NOME DO AUTOR","ano":1945}'
>>


ano          : 1945
autor        : NOME DO AUTOR
data_criacao : 2026-07-31 10:42:53.667221
id           : 5
titulo       : NOME DO LIVRO



PS H:\python\2-etapa\Aula15-API> Invoke-RestMethod http://127.0.0.1:5000/api/livros -Method POST -ContentType "application/json" -Body '{"titulo":"NOME DO LIVRO","autor":"NOME DO AUTOR","ano":1945}'
>>


ano          : 1945
autor        : NOME DO AUTOR
data_criacao : 2026-07-31 10:42:54.375201
id           : 6
titulo       : NOME DO LIVRO



PS H:\python\2-etapa\Aula15-API> Invoke-RestMethod http://127.0.0.1:5000/api/livros -Method POST -ContentType "application/json" -Body '{"titulo":"NOME DO LIVRO","autor":"NOME DO AUTOR","ano":1945}'
>>


ano          : 1945
autor        : NOME DO AUTOR
data_criacao : 2026-07-31 10:42:57.623734
id           : 7
titulo       : NOME DO LIVRO



PS H:\python\2-etapa\Aula15-API> Invoke-RestMethod http://127.0.0.1:5000/api/livros -Method POST -ContentType "application/json" -Body '{"titulo":"NOME DO LIVRO","autor":"NOME DO AUTOR","ano":1945}'
>>


ano          : 1945
autor        : NOME DO AUTOR
data_criacao : 2026-07-31 10:42:57.944628
id           : 8
titulo       : NOME DO LIVRO



PS H:\python\2-etapa\Aula15-API>
PS H:\python\2-etapa\Aula15-API> Invoke-RestMethod http://127.0.0.1:5000/api/livros -Method POST -ContentType "application/json" -Body '{"titulo":"NOME DO LIVRO","autor":"NOME DO AUTOR","ano":1945}'
>>


ano          : 1945
autor        : NOME DO AUTOR
data_criacao : 2026-07-31 10:42:58.669503
id           : 9
titulo       : NOME DO LIVRO



PS H:\python\2-etapa\Aula15-API> Invoke-RestMethod http://127.0.0.1:5000/api/livros -Method POST -ContentType "application/json" -Body '{"titulo":"NOME DO LIVRO","autor":"NOME DO AUTOR","ano":1945}'
>>


ano          : 1945
autor        : NOME DO AUTOR
data_criacao : 2026-07-31 10:42:59.151804
id           : 10
titulo       : NOME DO LIVRO



PS H:\python\2-etapa\Aula15-API> Invoke-RestMethod http://127.0.0.1:5000/api/livros -Method POST -ContentType "application/json" -Body '{"titulo":"NOME DO LIVRO","autor":"NOME DO AUTOR","ano":1945}'
>>


ano          : 1945
autor        : NOME DO AUTOR
data_criacao : 2026-07-31 10:42:59.539556
id           : 11
titulo       : NOME DO LIVRO



PS H:\python\2-etapa\Aula15-API> Invoke-RestMethod http://127.0.0.1:5000/api/livros -Method POST -ContentType "application/json" -Body '{"titulo":"NOME DO LIVRO","autor":"NOME DO AUTOR","ano":1945}'
>>


ano          : 1945
autor        : NOME DO AUTOR
data_criacao : 2026-07-31 10:42:59.875211
id           : 12
titulo       : NOME DO LIVRO



PS H:\python\2-etapa\Aula15-API> Invoke-RestMethod http://127.0.0.1:5000/api/livros -Method POST -ContentType "application/json" -Body '{"titulo":"NOME DO LIVRO","autor":"NOME DO AUTOR","ano":1945}'
>>


ano          : 1945
autor        : NOME DO AUTOR
data_criacao : 2026-07-31 10:43:00.238501
id           : 13
titulo       : NOME DO LIVRO



PS H:\python\2-etapa\Aula15-API> Invoke-RestMethod http://127.0.0.1:5000/api/livros -Method POST -ContentType "application/json" -Body '{"titulo":"NOME DO LIVRO","autor":"NOME DO AUTOR","ano":1945}'
>>


ano          : 1945
autor        : NOME DO AUTOR
data_criacao : 2026-07-31 10:43:00.589339
id           : 14
titulo       : NOME DO LIVRO



PS H:\python\2-etapa\Aula15-API> Invoke-RestMethod http://127.0.0.1:5000/api/livros -Method POST -ContentType "application/json" -Body '{"titulo":"NOME DO LIVRO","autor":"NOME DO AUTOR","ano":1945}'
>>


ano          : 1945
autor        : NOME DO AUTOR
data_criacao : 2026-07-31 10:43:00.938565
id           : 15
titulo       : NOME DO LIVRO



PS H:\python\2-etapa\Aula15-API> Invoke-RestMethod http://127.0.0.1:5000/api/livros/1 `
>>    -Method PUT `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"Cotemig","autor":"3A1","ano":2026}'


ano          : 2026
autor        : 3A1
data_criacao : 2026-07-28 08:07:18.167187
id           : 1
titulo       : Cotemig



PS H:\python\2-etapa\Aula15-API> Invoke-RestMethod http://127.0.0.1:5000/api/livros/5 `
>>    -Method PUT `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"Cotemig","autor":"3A1","ano":2026}'


ano          : 2026
autor        : 3A1




data_criacao : 2026-07-31 10:42:53.667221
id           : 5
titulo       : Cotemig



PS H:\python\2-etapa\Aula15-API> Invoke-RestMethod http://127.0.0.1:5000/api/livros/5  -Method DELETE `
>>

PS H:\python\2-etapa\Aula15-API> Invoke-RestMethod http://127.0.0.1:5000/api/livros/3  -Method DELETE `
>>

PS H:\python\2-etapa\Aula15-API>


