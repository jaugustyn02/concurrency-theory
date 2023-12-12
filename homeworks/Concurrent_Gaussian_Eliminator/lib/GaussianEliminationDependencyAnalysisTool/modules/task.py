class Task:
    def __init__(self, string: str):
        self.type = self.read_task_type(string)

        if self.type == 'A':
            self.i, self.k = self.read_A_indices(string)
        elif self.type == 'B':
            self.i, self.j, self.k = self.read_B_indices(string)
        elif self.type == 'C':
            self.i, self.j, self.k = self.read_C_indices(string)
        else:
            raise Exception('Invalid task type')
        
    def read_task_type(self, string: str):
        return string[0]
    
    def read_A_indices(self, A: str):
        return int(A[1])-1, int(A[3])-1
    
    def read_B_indices(self, B: str):
        return int(B[1])-1, int(B[3])-1, int(B[5])-1
    
    def read_C_indices(self, C: str):
        return int(C[1])-1, int(C[3])-1, int(C[5])-1
