def count():
    f=open("17. display and count number of vowels and consonants.txt")
    Vowels=['A','E','I','O','U']
    a=f.read()
    consonants=0
    vowels=0
    for i in a:
        j=i.upper()
        if (j.isalpha()) and (j not in Vowels):
            consonants+=1
        elif (j.isalpha()) and (j in Vowels):
            vowels+=1
    print("Number of vowels: ",vowels)
    print("Number of consonants: ",consonants)
    f.close()
count()
        
