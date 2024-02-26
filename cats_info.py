def get_cats_info(path):
    cats_list = []
    with open(path, 'r') as file:
        for line in file:
            cat_id, name, age = line.strip().split(',')
            cat_info = {'id': cat_id, 'name': name, 'age': int(age)}
            cats_list.append(cat_info)
    return cats_list

cats_info = get_cats_info('cats_info.txt')

print(cats_info)











































































"""def get_cats_info(path):
    cats_list = []
    with open(path, 'r') as file:
        for line in file:
            
            cat_id, name, age = line.strip().split(',')
            
            cat_info = {
                'id': cat_id,
                'name': name,
                'age': int(age)  
            }
            
            cats_list.append(cat_info)
    return cats_list


file_path = 'cats_info.txt'


cats_info = get_cats_info(file_path)


for cat in cats_info:
    print(f"ID: {cat['id']}, Name: {cat['name']}, Age: {cat['age']}")"""
