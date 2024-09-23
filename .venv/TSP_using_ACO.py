import random
n = int(input())
p = 0.2
dict_path = {}
for i in range(n):
    for j in range(i+1, n):
        value = random.randint(1, 100) 
        dict_path[(i, j)] = value
        dict_path[(j, i)] = value
dict_intensity = {(i,j): 1.0 for i in range(n) for j in range(n) if i != j}
def prob_sum(i, choice):
    sum = 0
    for j in choice:
        sum += dict_intensity[(i, j)] * 1/dict_path[(i,j)]
    return sum
iterations = 0
while iterations<100:
    temp = None
    min_path = 1e9
    x = {i: 0 for i in range(n)}
    iterations += 1
    general_path = {}
    for i in range(n):
        choice = [j for j in range(n) if j != i]
        path = [i]
        while len(path) < n:
            sum = prob_sum(path[-1],choice)
            choice_prob = [(dict_intensity[(path[-1], j)] /dict_path[(path[-1],j)])/sum for j in choice]
            next_city = random.choices(choice, weights=choice_prob)[0]
            path.append(next_city)
            choice.remove(next_city)
        general_path[i] = path + [i]
        for j in range(1,n):
            x[i] += dict_path[(path[j-1], path[j])]
        if(x[i] < min_path):
            min_path = x[i]
            temp = path + [i]
    for i in range(n):
        temp_path = general_path[i]
        for j in range(1,n):
            dict_intensity[(temp_path[j-1], temp_path[j])] += 1/x[i]
            dict_intensity[(temp_path[j],temp_path[j-1])] += 1/x[i]
    for i in range(n):
        for j in range(i+1, n):
            dict_intensity[(i,j)] = dict_intensity[(i,j)]*(1-p)
            dict_intensity[(j,i)] = dict_intensity[(j,i)]*(1-p)
    print(f'Iteration {iterations}, Min cost: {min_path}, Path: {temp}')
