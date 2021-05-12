eq1 = input("Enter the first equation:\n")
eq2 = input("Enter the second equation:\n")
value_dict1 = {"x":0, "y":0, "constant": 0}
value_dict2 = {"x":0, "y":0, "constant": 0}
indexes_list = []
coefficient = []
for i in range(len(eq1)): #1.equation to simple
    if eq1[i] == "+" or eq1[i] == "-":
        indexes_list.append(i)
for i in range(len(indexes_list)):
    if i == len(indexes_list)-1:
        coefficient.append(eq1[indexes_list[i]:])
    else:
        coefficient.append(eq1[indexes_list[i]:indexes_list[i+1]])
counter = 0
while not coefficient[counter].endswith("="):
    if coefficient[counter].endswith("x"):
        coefficient[counter] = coefficient[counter].replace("x","")
        value_dict1["x"] += int(coefficient[counter])
    elif coefficient[counter].endswith("y"):
        coefficient[counter] = coefficient[counter].replace("y","")
        value_dict1["y"] += int(coefficient[counter])
    else:
        value_dict1["constant"] -= int(coefficient[counter])
    counter +=1 
coefficient[counter]=coefficient[counter].replace("=","")
if coefficient[counter].endswith("x"):
    coefficient[counter] = coefficient[counter].replace("x","")
    value_dict1["x"] += int(coefficient[counter])
elif coefficient[counter].endswith("y"):
    coefficient[counter] = coefficient[counter].replace("y","")
    value_dict1["y"] += int(coefficient[counter])
else:
    value_dict1["constant"] -= int(coefficient[counter])
counter +=1 
while counter < len(coefficient):
    if coefficient[counter].endswith("x"):
        coefficient[counter] = coefficient[counter].replace("x","")
        value_dict1["x"] -= int(coefficient[counter])
    elif coefficient[counter].endswith("y"):
        coefficient[counter] = coefficient[counter].replace("y","")
        value_dict1["y"] -= int(coefficient[counter])
    else:
        value_dict1["constant"] += int(coefficient[counter])
    counter += 1
counter = 0 #2.equation to simple
indexes_list = []
coefficient = []
for i in range(len(eq2)):
    if eq2[i] == "+" or eq2[i] == "-":
        indexes_list.append(i)
for i in range(len(indexes_list)):
    if i == len(indexes_list)-1:
        coefficient.append(eq2[indexes_list[i]:])
    else:
        coefficient.append(eq2[indexes_list[i]:indexes_list[i+1]])
counter = 0
while not coefficient[counter].endswith("="):
    if coefficient[counter].endswith("x"):
        coefficient[counter] = coefficient[counter].replace("x","")
        value_dict2["x"] += int(coefficient[counter])
    elif coefficient[counter].endswith("y"):
        coefficient[counter] = coefficient[counter].replace("y","")
        value_dict2["y"] += int(coefficient[counter])
    else:
        value_dict2["constant"] -= int(coefficient[counter])
    counter +=1 
coefficient[counter]=coefficient[counter].replace("=","")
if coefficient[counter].endswith("x"):
    coefficient[counter] = coefficient[counter].replace("x","")
    value_dict2["x"] += int(coefficient[counter])
elif coefficient[counter].endswith("y"):
    coefficient[counter] = coefficient[counter].replace("y","")
    value_dict2["y"] += int(coefficient[counter])
else:
    value_dict2["constant"] -= int(coefficient[counter])
counter +=1 
while counter < len(coefficient):
    if coefficient[counter].endswith("x"):
        coefficient[counter] = coefficient[counter].replace("x","")
        value_dict2["x"] -= int(coefficient[counter])
    elif coefficient[counter].endswith("y"):
        coefficient[counter] = coefficient[counter].replace("y","")
        value_dict2["y"] -= int(coefficient[counter])
    else:
        value_dict2["constant"] += int(coefficient[counter])
    counter += 1
if value_dict1["y"]>=0:
    value_dict1["y"] ="+{}".format(value_dict1["y"])
if value_dict2["y"]>=0:
    value_dict2["y"] ="+{}".format(value_dict2["y"])
print("Equations in the simplified form:") #print the simple
print("{}x{}y={}".format(value_dict1["x"],value_dict1["y"],value_dict1["constant"]))
print("{}x{}y={}".format(value_dict2["x"],value_dict2["y"],value_dict2["constant"]))
if value_dict1["x"]*value_dict2["x"] ==0:
    if value_dict1["x"] == 0:
        solution_y = int(value_dict1["constant"]/int(value_dict1["y"]))
        solution_x = int((value_dict2["constant"] - (int(value_dict2["y"])*solution_y)) / value_dict2["x"])
    else:
        solution_y = value_dict2["constant"]/int(value_dict2["y"])
        solution_x = (value_dict1["constant"] - (int(value_dict1["y"])*solution_y)) / value_dict1["x"]
elif value_dict1["x"]* value_dict2["x"] < 0:
    total_y = (abs(value_dict2["x"])*int(value_dict1["y"]))+ (abs(value_dict1["x"])*int(value_dict2["y"]))
    total_consant = (abs(value_dict2["x"])*value_dict1["constant"])+ (abs(value_dict1["x"])*value_dict2["constant"])
    solution_y = int(total_consant/total_y)
    solution_x = int((value_dict1["constant"]-(int(value_dict1["y"])*solution_y))/value_dict1["x"])
elif value_dict1["x"]* value_dict2["x"] > 0:
    total_y = (value_dict2["x"]*int(value_dict1["y"])*(-1))+ (value_dict1["x"]*int(value_dict2["y"]))
    total_consant = (value_dict2["x"]*value_dict1["constant"]*(-1))+ (value_dict1["x"]*value_dict2["constant"])
    solution_y = int(total_consant/total_y)
    solution_x = int((value_dict1["constant"]-(int(value_dict1["y"])*solution_y))/value_dict1["x"])
print("Solution:\nx={}\ny={}".format(solution_x,solution_y))