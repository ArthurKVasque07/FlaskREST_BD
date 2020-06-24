from models import Pessoas, Usuarios


# insere dados na tabela
def insere_pessoas():
    pessoa = Pessoas(nome='Bruno', idade=22)
    print(pessoa)
    pessoa.save()

# consulta dados na tabela
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Bruno').first()
    print(pessoa.idade)

# altera dados
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Bruno').first()
    pessoa.nome = 'Ricardo'
    pessoa.save()

# exclui dados na tabela
def excluir_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Ricardo').first()
    pessoa.delete()

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)


if __name__ == '__main__':
    insere_usuario('leandro', '1234')
    insere_usuario('juliana', '0710')
    consulta_todos_usuarios()
    # insere_pessoas()
    # altera_pessoa()
    # excluir_pessoa()
    # consulta_pessoas()
