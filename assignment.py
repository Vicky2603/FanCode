import requests

BASE_URL = "https://jsonplaceholder.typicode.com/"

def json_content(end_point):
    response = requests.get(BASE_URL+end_point)
    json_content = response.json()
    return json_content

def get_fancode_users(end_point, user_id):
    user_id -= 1
    json = json_content(end_point)
    
    lat = float(json[user_id]['address']['geo']['lat'])
    lng = float(json[user_id]['address']['geo']['lng'])
    if (lat <= 40 and lat >= -5):
        if (lng <= 100 and lng >= 5):
            return json[user_id]
    return False


def get_todos_with_user_id(end_point, user_id):
#     user_id -= 1
    json = json_content(end_point)
    json = json[20*(user_id-1): 20*user_id]
    completed_count = 0
    not_Completed_count = 0
    total_count = 0
    
    for i in range(len(json)):
        if json[i]['completed'] == True:
            completed_count += 1
        elif json[i]['completed'] == False:
            not_Completed_count += 1
        total_count += 1
        
    percentage = (completed_count / total_count) * 100
    if percentage >= 50:
        return 'User Completed task more than 50%'
    return f'Incomplete task is more than the completed task. user has only {percentage}%'



if __name__ == '__main__':
    user_id = 7 
    result = get_fancode_users('users', user_id)
    
    if result:  # if condition is to check the fancode user
        print(get_todos_with_user_id('todos', user_id))
    else:
        print("Not a fancode user")
