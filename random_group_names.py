import random

if __name__ == '__main__':
    group_names = ["Charming P*", "Naughty Solution","Impossible Technology", "Bloody Television","Black Girl","30cm Python","Mushy Bread","Success Impossible"]
    random_groups = [group_names[random.randrange(len(group_names))] for _ in group_names]
    filtered_groups = list(set(random_groups))
    print(filtered_groups)
    