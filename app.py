print("Hello World")

Age =20

first_name= "Aba"
is_online =True


print(f"The age of {Age} of {first_name}. Online Status: {is_online}") 



patients = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Samatar', 'age': 25},
    {'name': 'Charlie', 'age': 45},
    
]


def get_patient(patients):
    
    if len(patients)>=2:
        return patients[1]
    else:
        return "There are not enough patients"
    

second_patient_info = get_patient(patients)

second_patient_list = [second_patient_info]

print (second_patient_list)


name = input("What is your name? " )

print("Hello " + name)

age= int(input("what is your age? : "))




list_of_new_patients=[]

list_of_new_patients.append({"name": name, "age": age})

print("list of new patients: ", list_of_new_patients)


birth_year = input ("Enter birth year: ")


birth_age = 2024 - int(birth_year)

print (birth_age)

first = float(input("First: "))
second = float(input("Second: "))

sum= first + second

print("Sum: " + str(sum))

