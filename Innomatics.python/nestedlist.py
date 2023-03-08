if __name__ == '__main__':
    
    n = int(input())
    
    records = []
   
    for i in range(n):
        name = input()
        score = float(input())
        
        records.append([name, score])
    
    sorted_records = sorted(records, key=lambda x: x[1])
    
    second_lowest_grade = sorted(set([record[1] for record in sorted_records]))[1]
    
    second_lowest_students = [record[0] for record in sorted_records if record[1] == second_lowest_grade]
    
    second_lowest_students.sort()
    
    for student in second_lowest_students:
        print(student)
