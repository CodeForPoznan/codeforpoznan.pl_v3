import csv

with open('list.csv') as csv_file:
    rows = []
    list_of_users = []

    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        rows.append(row)

    dates = rows[0][4:]

    users_dict = {
        "id": "",
        "github": "",
        "first_name": "",
        "last_name": "",
        "email": "",
        "phone": ""
    }

    rows = rows[1:]
    for item in rows:
        # import sys
        # import pdb
        # sys.stdout = sys.__stdout__
        # pdb.set_trace()
        _id, github, name, phone, email, *values = item
        try:
            first_name = name.split()[0]
        except:
            pass
        try:
            last_name = name.split()[1]
        except:
            pass

        users_dict["id"] = _id
        users_dict["github"] = github
        users_dict["first_name"] = first_name
        users_dict["last_name"] = last_name
        users_dict["email"] = email
        users_dict["phone"] = phone

        list_of_users.append(users_dict)

        users_dict = {
            "id": "",
            "github": "",
            "first_name": "",
            "last_name": "",
            "email": "",
            "phone": ""
        }

    import sys
    import pdb
    sys.stdout = sys.__stdout__
    pdb.set_trace()
