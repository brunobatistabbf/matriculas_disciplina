from abc import ABC, abstractmethod
#abc proporciona um comportamento parecido com interfaces em JAVA
class DisciplinaInterface(ABC):
    @abstractmethod
    def realizar_matricula(self, aluno):
        pass
    @abstractmethod
    def exibir_alunos_matriculados(self):
        pass

class Disciplina(DisciplinaInterface):
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo
        self.alunos_matriculados = []

    def realizar_matricula(self, aluno):
        if aluno not in self.alunos_matriculados:
            self.alunos_matriculados.append(aluno)
            print(f"{aluno} matriculado na disciplina {self.nome}")
        else:
            print(f"{aluno} já está matriculado na disciplina {self.nome}")

    def exibir_alunos_matriculados(self):
        print(f"\nAlunos matriculados na disciplina {self.nome}:")
        for aluno in self.alunos_matriculados:
            print(aluno)

if __name__ == "__main__":
    disciplina = Disciplina(nome="Portugues", codigo="PRT167")

    disciplina.realizar_matricula("Bruno Batista")
    disciplina.realizar_matricula("Carlos Eduardo")
    disciplina.realizar_matricula("Fernando Matos")

    disciplina.exibir_alunos_matriculados()
