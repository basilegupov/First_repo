lines=[['60b90c1c13067a15887e1ae1', 'Tayson', '3'], ['60b90c2413067a15887e1ae2', 'Vika', '1'], ['60b90c2e13067a15887e1ae3', 'Barsik', '2']]
for i in range(len(lines)):
    print(lines[i])
    lines[i] = {"id":lines[i][0], "name": lines[i][1], "age": lines[i][2]}
    # for j in range(len(lines[i])):
    #     print(lines[i][j])
    #     lines[i][j]={"id":lines[i][j]}


print(lines)



from collections import defaultdict

req = [[1,5,8],
       [2,6,7],
       [1,6,8],
       [2,6,7],
       [1,6,8],
       [6,3,1],
       [9,11,4],
       [11,6,8],
       [5,9,7],
       [4,6,8],
       [10,11,3]]
rases = players = [i for i in range(1,12)]
result = {}
print(rases, players)

# while len(rases)>0 and len(players)>0:
#     pass1 = [req[i][0] for i in range(len(req))]
#     print(pass1)
#     pass1_frequency = defaultdict(list)
#     i = 1
#     for rasa in pass1:
#         pass1_frequency[rasa].append(i)
#         i += 1
#     for rasa, player in pass1_frequency.items:
#         if rasa in rases player in players:

#             if len(player) == 1:
#                 result[rasa]=player
#                 rases.pop(rasa)
#                 players.pop(player)
#             elif

    
    # print(pass1_frequency)


def sanitize_file(source, output):
    with open(source, 'r') as file_i:
        data = file_i.readlines()
        data = [line.replace('0', '').
                replace('1', '').
                replace('2', '').
                replace('3', '').
                replace('4', '').
                replace('5', '').
                replace('6', '').
                replace('7', '').
                replace('8', '').
                replace('9', '')
                 for line in data]
    print(data)
    with open(output, 'w') as file_o:
        for line in data:
            file_o.write(line)
    
ff = sanitize_file('1.txt', '2.txt')    
