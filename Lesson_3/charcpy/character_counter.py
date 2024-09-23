from .character_counter_result import CharacterCounterResult

class CharacterCounter:
    def __init__(self, file_path, skip_lines=0, print_stats=False):
        """
        Initialize the class with the input file path and optional arguments.
        
        Parameters:
        file_path : str
            Path to the input file
        skip_lines : int
            Number of lines to skip in the input file, default 0
        print_stats : bool
            Print statistics of the file (number of characters, number of words, number of lines), default False
        """
        self.file_path = file_path
        self.skip_lines = skip_lines
        self.print_stats = print_stats
        self.result = CharacterCounterResult(file_path, skip_lines, print_stats)
        
        
    def character_count(self,string):
        """Counts the number of characters in a string and updates the result dictionary.

        Args:
            string: The string to count the characters of
        """
        num_of_characters=0
        for char in string.lower():
            if char in self.result:
                num_of_characters+=1
                self.result[char]+=1
        self.result.number_of_characters+=num_of_characters

    def process_line(self, line):
        """
        Process a single line of the input file.
        
        Parameters:
        line : str
            Line of the input file
        """
        
        if not self.print_stats:
            self.character_count(line)
        else:
            words=line.lower().split()
            len_words=len(words)
            if len_words>0:             #avoid empty lines
                self.result.number_of_lines+=1
                for word in words:
                    self.character_count(word)
                self.result.number_of_words+=len_words
    def run(self):
        """
        Run the character counting script.
        """
        with open(self.file_path, "r") as file:
            counter=0
            for line in file:
                counter+=1
                if counter <= self.skip_lines:
                    continue
                self.process_line(line)
        for key, value in self.result.items():
            self.result[key]=value/self.result.number_of_characters*100
