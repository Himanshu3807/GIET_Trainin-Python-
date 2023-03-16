def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    result=[0,0,0]
    i=1 
    while(i<len(patient_medical_speciality_list)):
        if patient_medical_speciality_list[i]=='P':
            result[0]=result[0]+1
        elif patient_medical_speciality_list[i]=='O':
            result[1]=result[1]+1
        else:result[2]=result[2]+1
        i=i+2
    a=max(result)
    a=result.index(a)
    if a==0:speciality='Pediatrics'
    elif a==1:speciality='Orthopedics'
    else:speciality='ENT'
    return speciality
patient_medical_speciality_list=[301,'O',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)
