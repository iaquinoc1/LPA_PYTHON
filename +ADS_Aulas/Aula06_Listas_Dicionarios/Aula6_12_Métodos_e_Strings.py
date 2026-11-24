#Manipulação de Strings
#Strings são imutáveis, a menos que sejam convertidas em listas

#Relação de métodos para uso com strings

# startswith >> Verifica se caracteres existem no início da string
# endswith >> Verifica se caracteres existem no final da string
# lower >> Converte string para minúscula
# upper >> Converte string para maiúscula
# find >> Busca a primeira ocorrência de um padrão de caracteres em uma string
# rfind >> Idêntico ao find, mas inicia a busca da direita para a esquerda
# center >> Centraliza uma string
# ljust, rjust >> Ajustam uma string com alinhamentos à esquerda ou à direita, respectivamente
# split >> Divide uma string
# replace >> Substitui caracteres em uma string
# lstrip, rstrip >> Removem espaços em branco à esquerda ou à direita, respectivamente
# strip >> Remove espaços em branco das extremidades

s1 = list("Algoritmos") #Transforma string em lista
print (s1) #Print imprime carcateres separados, por ser uma lista
print (''.join(s1)) #Método 'join' (juntar) para imprimir os carecteres juntos

s1[0] = 'a' #Possível alterar caracter a partir do índice ('a' minúsculo)
print (''.join(s1))

print (' ')

s1 = 'Lógica de Programação e Algoritmos'
print(s1.upper()) #Converte todas pra maiúsculo
print(s1.lower()) #Converte todas pra minúsculo
print(s1.count('a')) #Contagem de letras 'a'
print(s1.lower().count('a'))

print (' ')

print(s1.split(' ')) #Quebrando a string em listas

print (' ')

print (s1.replace('a', 'A', 1)) #Substituição de valores na string, 1 vez


#Outros métodos com strings para verificação de cadastros e senhas:
#**Função/método — Retorna *True* para uma *string* com...**

#**isalnum:** Somente letras e números; acentos são aceitos
#**isalpha:** Somente letras; acentos são aceitos
#**isdigit:** Somente números
#**isnumeric:** Somente números; aceita também caracteres matemáticos, como frações
#**isupper:** Somente caracteres maiúsculos
#**islower:** Somente caracteres minúsculos
#**isspace:** Somente espaços; inclui TAB, quebra de linha, retorno etc.
#**isprintable:** Somente caracteres possíveis de serem impressos na tela

print (s1.isalnum()) #Teste somente caracteres alfanuméricos
print (s1.isalpha()) #Teste somente caracteres alfabéticos