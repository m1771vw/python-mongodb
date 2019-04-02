from pymongo import MongoClient

if __name__ == "__main__":

    myclient = MongoClient("mongodb://localhost:27017/")
    mydb = myclient["pythontest"]
    mycol = mydb["test"]

    mydict = {
        "name": "William Yang",
        "age": 26,
        "email": "wyang93@gmail.com"
    }
    # print(mycol.insert_one(mydict).inserted_id)
    mylist = [
        { "name": "Megan Tran", "age": 25, "email": "m_Tran@gmail.com"},
        { "name": "Stephanie Tran", "age": 25, "email": "s_Tran@gmail.com"},
        { "name": "Young Kim", "age": 27, "email": "ykim@gmail.com"},
        { "name": "Adrian Ho", "age": 27, "email": "adrian_ho@gmail.com"},
        { "name": "Cynthia Duong", "age": 22, "email": "c_duong@gmail.com"},
        { "name": "Henry Rodriguez", "age": 23, "email": "henryrodriguez@gmail.com"},
        { "name": "Ethan Wang", "age": 25, "email": "ewang@gmail.com"},
    ]
    # print(mycol.insert_many(mylist).inserted_ids)
    # for x in mycol.find():
    #     print(x)

    # for x in mycol.find():
    #     print(x)
    
    for x in mycol.find(
        { "name": { "$regex" : "il"}},
        { "name": 1, "age": 1}
    ):
        print(x)

