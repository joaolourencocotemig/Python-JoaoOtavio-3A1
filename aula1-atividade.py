from flask import Flask


app = Flask(__name__) # inicio o flask

@app.route('/') # Isso é o decorator, ele é usado para mapear a função abaixo para a rota '/'
def ola_mundo():
    return 'Olá, Mundo!' # Isso é o que será retornado quando a rota '/' for acessada

@app.route('/decorator')
def explicar_decorator():
    texto_explicativo = """
    <h1>Entendendo Decorators em Python</h1>
    
    <h2>1. O que é um decorator?</h2>
    <p>Em Python, um <b>decorator</b> é uma função que envolve (ou "decora") outra função. Ele permite que você modifique o comportamento da função original sem alterar o código-fonte dela permanentemente.</p>
    
    <h2>2. Para que serve?</h2>
    <p>Eles são usados para adicionar funcionalidades extras a funções existentes de forma reutilizável. Exemplos comuns incluem:</p>
    <ul>
        <li>Verificação de autenticação (se o usuário está logado).</li>
        <li>Registro de logs (para monitoramento).</li>
        <li>Medição de tempo de execução.</li>
    </ul>
    
    <h2>3. Como é utilizado no Flask? (Exemplo: @app.route)</h2>
    <p>No Flask, os decorators são essenciais para mapear URLs para funções específicas. Quando você usa o <code>@app.route('/decorator')</code>, você está dizendo ao Flask:</p>
    <ul>
        <li>Pegue a função <code>explicar_decorator()</code> definida logo abaixo.</li>
        <li>"Decore-a" transformando-a em uma rota web.</li>
        <li>Sempre que um usuário acessar o caminho <code>/decorator</code> no navegador, execute esta função.</li>
    </ul>
    """
    return texto_explicativo


if __name__ == '__main__':
    app.run(debug=True) # Isso inicia o servidor Flask em modo de depuração, o que é útil para desenvolvimento
