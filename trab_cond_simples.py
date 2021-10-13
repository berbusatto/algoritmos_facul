# O  SENAC  oferece  cursos  presenciais  em  diversas  áreas.  Por  serem  presenciais,  exige-se  que  o
# aluno esteja presente em, no mínimo, 75 % das aulas. Criar um algoritmo que leia a quantidade de
# aulas ministradas e a quantidade de aulas que o aluno faltou. Após essa leitura, informar se o alunos
# está ou não reprovado por faltas.
# Tendo  informado  se  o  aluno  está  ou  não  reprovado  por  falta,  o  algoritmo  deve  mostrar  a  seguinte
# mensagem  na  tela:  “Deseja  realizar  a  matrícula para o próximo semestre ?”. Se a resposta for ‘S’,
# mostrara mensagem: “A matrícula deverá ser realizada até o dia 10”. Se a resposta for ‘N’, mostrar
# mensagem: “Sua matrícula será trancada”.

carga_horaria = int(input('Carga horária da disciplina: '))
qtd_faltas = int(input('Faltas: '))
limite = carga_horaria * 0.25

if qtd_faltas <= limite:
    print('Não reprovado por falta')
else:
    print('Reprovado por falta')
matricula = input('Deseja realizar a matrícula para o próximo semestre? S ou N ')
if matricula.lower() == 's':
    print('A matrícula deverá ser realizada até o dia 10')
elif matricula.lower() == 'n':
        print('Sua matrícula será trancada')






