class Foo:
    startId=310000
    def __call__(self):
        Foo.startId+=1
sol=Foo()
with open('input.txt','r') as input:
    data=input.read()
    data=data.replace("Examples:","@TC:\n"+"    Examples:")
    data=data.replace("Scenario:","@TC:\n"+"Scenario:")
    data=data.replace("@TC:","@TC:"+str(sol()))
    with open('output.txt','w') as output:
        output.write(data)
