def input_matrix():
    rows=int(input("Enter Number of Rows: "))
    columns=int(input("Enter Number of Columns: "))
    matrix=[]
    
    for i in range(rows):
        matrix.append([])

        for j in range(columns):
            matrix[i].append(int(input(f"Enter Number at [{i}][{j}]: ")))

    return matrix


def addition_matrix(matrix_1,matrix_2):
    added_matrix=[]
    for i in range(len(matrix_1)):
        added_matrix.append([])

        for j in range(len(matrix_1[1])):
            added_matrix[i].append(matrix_1[i][j]+matrix_2[i][j])

    return added_matrix
        

def multiplication_matrix(matrix_1, matrix_2):
    multiplied_matrix = []

    for i in range(len(matrix_1)):
        multiplied_matrix.append([])

        for j in range(len(matrix_2[0])):
            total = 0

            for k in range(len(matrix_2)):
                total += matrix_1[i][k] * matrix_2[k][j]

            multiplied_matrix[i].append(total)

    return multiplied_matrix
        
            

def transpose_matrix():
    pass

def deteminate():
    pass

def main():
    matrix_1=[[1,2,3],
              [2,3,4],
              [3,5,6]]
    
    matrix_2=[[2,3,4],
              [1,2,2],
              [4,2,1]]
    
    print(multiplication_matrix(matrix_1,matrix_2))

if __name__=="__main__":
    main()
