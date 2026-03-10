#1. Count the occurrence of substring

def count_occurrence(s,sub):
    count = 0
    for i in range(len(s)-len(sub)+1):
        if s[i:i+len(sub)]==sub:
            count += 1
    return count
print(count_occurrence("aaaa","aa"))

#2. Division

def division(a,b):
    if b == 0:
        return "MAN"
    else:
        return a/b
print(division(15,0))

#3.income, credit score

def loan_approval(income, credit_score, debt):
    debt_ratio = debt/income
    if income >= 50000 and credit_score >= 700 and debt_ratio < 0.3 :
        return "Eligible" 
    elif income >= 30000 and credit_score >= 600 and debt_ratio < 0.5:
        return "Review"
    else:
        return "Reject"
print(loan_approval(60000,650,10000))   

#4.discount

def discount_amount(amount):
    if amount < 1000:
        discount = 0
    elif amount < 5000:
        discount = 0.05
    else:
        discount = 0.10
    return amount - (amount*discount)
print(discount_amount(6000))

#5. replace string with #

s = "Welcome All"
result = ""
for ch in s:
    if ch == " ":
        result += " "
    else:
        result += "#"
print(result)

#6.square for even no cube for odd

def square_cubes(arr):
    result = []
    for num in arr:
        if (num % 2) == 0:
            result.append(num ** 2)
        else:
            result.append(num ** 3)
    return result
print(square_cubes([1,2,3,4]))

#7.password attempts

def password_attempts(correct_pwd):
    attempts = 3
    while attempts > 0:
        pwd = input("Enter a password:")
        if pwd == correct_pwd:
            print("Access Granted")
            return
        else:
            attempts -= 1
            print("Wrong Password. NO of attempts left", attempts)
    print("Account Locked")
password_attempts("admin123")

#8.convert into title case

def tittle_case(sentence):
    special = {"AI", "ML"}
    words = sentence.split()
    result = []
    for word in words:
        if word.upper() in special:
            result.append(word.upper())
        else:
            result.append(word.capitalize())
    return " ".join(result)
print(tittle_case("Ai and ml are powerful"))

#9.Multiple times

def multipulication_tables(N):
    for i in range(1,N+1):
        print(f"\nTable of {i}")
        for j in range(1,11):
            print(f"{i} x {j} = {i*j}")
multipulication_tables(10)

