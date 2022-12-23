with open('generated.txt', 'r') as f:
    x = f.readlines()


dictionary = dict.fromkeys(x)
deduplicated_list = list(dictionary)
print(len(deduplicated_list))


with open('de_dep.txt', 'a') as f:
    [f.write(i) for i in deduplicated_list if len(i) > 0]
