import json

def read_json_file(file):
    with open(file,"r") as file:
        data = json.load(file)
    print(data)

def write_data_into_json_file(file,data):
    with open(file,"a") as file:
        json.dump(data,file,indent=4)

def update_data_into_json_file(file1,data1):
    with open(file1,"r") as file:
        data = json.load(file)

    # print(type(data))
    data.append(data1)
    with open(file1,"w") as file:
        json.dump(data,file,indent=4)

def delete_data_from_json_file(file1,id):
    with open(file1,"r") as file:
        data = json.load(file)
    new_data = []
    for i in data:
        if i["id"] != id:
            new_data.append(i)        

    with open(file1,"w") as file:
        json.dump(new_data,file,indent=4)


# employees = [
#     {"id": 1, "name": "Alice", "age": 25},
#     {"id": 2, "name": "Bob", "age": 30}
# ]
# write_data_into_json_file("demo.json",employees)
# read_json_file("demo.json")

# employees = {"id": 4, "name": "mayur", "age": 27}
# update_data_into_json_file("demo.json",employees)

delete_data_from_json_file("demo.json",2)





# dist1 ={
#     "lname":"baviskar"
# }

# with open("demo.json","r") as file:
#     data1 = json.load(file)

# data1["name"]="mayur"

# with open("demo.json","a") as file:
#     json.dump(data1,file)


# with open("demo.json","r") as file:
#     data = json.load(file)

# print(data)