import io
from string import Template
import inquirer
cargos = [
  inquirer.List('cargos',
                message="Qual seu cargo no RobSIC?",
                choices=['Diretor', 'Vice-diretor', 'Pesquisador', 'Aluno, B.Sc.', 'Aluno, M.Sc.', 'Aluno, Ph.D.'],
            ),
]


nome = input("Digite seu nome completo.")
email = input("Digite seu email @unifei")
cargo = inquirer.prompt(cargos)
# print(cargo["cargos"])

