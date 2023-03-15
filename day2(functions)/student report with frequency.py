lst_of_marks=(12,18,25,24,2,5,18,20,20,21)
def find_more_than_average():
    marks=0
    count=0
    for x in lst_of_marks:
        marks+=x
    average=marks/len(lst_of_marks)
    for x in lst_of_marks:
        if x>average:
            count+=1
    percentage=(count*100)/len(lst_of_marks)
    return percentage
def sort_marks():
    global lst_of_marks
    lst_of_marks=sorted(lst_of_marks)
    return lst_of_marks
def generate_frequency():
    freq=[]
    for x in range(26):
        count=0
        for y in lst_of_marks:
            if x==y:
                count+=1
        freq.append(count)
    return freq
print(find_more_than_average())
print(generate_frequency())
print(sort_marks())
