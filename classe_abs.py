from abc import ABC, abstractmethod
#abc para marcar os metodos como abstratos
#Classe Abstrata
class Disciplina(ABC):
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo
        self.alunos_matriculados = []

    @abstractmethod
    def realizar_matricula(self, aluno):
        pass

    @abstractmethod
    def exibir_alunos_matriculados(self):
        pass

#Classe Concreta
class Matricula(Disciplina):
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
    matricula_disciplina = Matricula(nome="Matemática", codigo="MAT101")

    matricula_disciplina.realizar_matricula("Fernando Matos")
    matricula_disciplina.realizar_matricula("Carlos Eduardo")
    matricula_disciplina.realizar_matricula("Bruno Batista")

    matricula_disciplina.exibir_alunos_matriculados()
