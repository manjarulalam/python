try:
    with open('main.py','r',encoding='utf-8') as file:
        # file.write("hello, i am now create a new file in python\n")
        content = file.read()
        print(content)
        print("success to create file")
except Exception as err:
    print(err)


try:
    with open('dpd.txt','w',encoding='utf-8') as file:
        file.write("hello, i am now create a new file in python\n")
        print("success to create file")
except Exception as err:
    print(err)