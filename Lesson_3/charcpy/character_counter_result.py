import string

class CharacterCounterResult(dict):
    def __init__(self, file_path, skip_lines=0, print_stats=False):
        self.file_path = file_path
        self.skip_lines = skip_lines
        self.print_stats = print_stats
        self.number_of_lines = 0
        self.number_of_words = 0
        self.number_of_characters = 0
        super().__init__({char : 0 for char in string.ascii_lowercase})
    
    def __str__(self):
        string_out=[]
        string_out += [f"file path: {self.file_path}"]
        if self.print_stats:
            string_out+=[f"number of non void lines: {self.number_of_lines}", f"lines skipped at beginning: {self.skip_lines}",
                         f"number of words: {self.number_of_words}", f"number of characters: {self.number_of_characters}"]
        for key, value in self.items():
            string_out.append(f"{key}: {value:.2f}%")
        return "\n".join(string_out)
    
    def plot_hist(self):
        import matplotlib.pyplot as plt
        plt.bar(self.keys(), self.values())
        plt.show()
