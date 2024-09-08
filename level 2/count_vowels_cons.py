# pass a string to a function
# count number of vowels & consonants 

vowels = ['a', 'e', 'i', 'o', 'u']

def counts_vow_cons(word):
    vow_count = 0                   
    cons_count = 0
    
    for i in range(len(word)):  
        if word[i].lower() in vowels:                #! convert it to lower case as we have lower case letters in 'vowels list'
            vow_count += 1
        else:
            cons_count +=1
    return vow_count , cons_count

vow_count , cons_count = counts_vow_cons("IslAm")

print(f"number of vowels : {vow_count}")
print(f"number of consonants : {cons_count}")


