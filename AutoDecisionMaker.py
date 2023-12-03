from random import choice

songs = [ ["eng pop","who says","IDGAF","Cool for the summer","Savage","Boss Bitch","Woman"],
["hin soft pop","tum mile","chale jaise hawayein", "jeet","liggi","Sage","Saibo","Iktara"],
["hin pop","Garmi","Saki Saki","Dilbar","Nachi nachi","Besharam rang","Jhoome jo pathan"],
["eng soft pop","cold/mess","2002","Mad at disney","Mood","Little do you know","Sorry","A thousand years"]
]

print("which mood u are in ?")
mood = input()

for item in songs:
    if(mood ==item[0]):
        print(mood + " song : " + choice(item[1:len(item)]))
    
