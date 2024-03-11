def meu_decorator(func):
    def wrapper():
        print("Antes da função ser chamada")
        func()
        print("Depois da função ser chamada")
    return wrapper


@meu_decorator
def minha_funcao():
    print("Minha função foi chamada")


minha_funcao()
