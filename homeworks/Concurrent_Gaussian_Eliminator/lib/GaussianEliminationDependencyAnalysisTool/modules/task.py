class Task:
    def __init__(self, string: str):
        self.type = self.read_task_type(string)

        if self.type == 'A':
            self.i, self.k = self.read_indices(string)
        elif self.type == 'B':
            self.i, self.j, self.k = self.read_indices(string)
        elif self.type == 'C':
            self.i, self.j, self.k = self.read_indices(string)
        else:
            raise Exception('Invalid task type')
        
    def read_task_type(self, string: str):
        return string[0]

    def read_indices(self, string: str):
        first_digit_index = 0
        while not string[first_digit_index].isdigit():
            first_digit_index += 1
        numbers = string[first_digit_index:].split('_')
        return [int(number)-1 for number in numbers]