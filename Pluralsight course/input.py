import json
with open("Ex1-Json.json",'r') as input:
    obj=json.load(input)
    print('hello,'+obj['name'])
    with open("output.txt",'w') as output:
        output.write(obj['name']+"'s hobbies are:\n")
        for hobby in obj['hobbies']:
            output.write(hobby+"\n")


