from hdn import Parser
import sys
'''
format in which progress data is stored:
    time_taken, raw_wpm, wpm, accuracy, date, time

'''

command = sys.argv[1]

class TrackPractice:
    def __init__(self, file):
        self.file = file
        self.parser = Parser(self.file)
    
    def enter_typing_data(self, time_taken, raw_wpm, wpm, accuracy, date, time):
        lines = [[time_taken, raw_wpm, wpm, accuracy, date, time]]
        self.parser.append(lines)
    
    def show_progress_text(self):
        lines = self.parser.parse()
        return lines

if command == 'show_progress':
    tp = TrackPractice('progress.hdn')
    lines = tp.show_progress_text()
    for line in lines:
        time_taken, raw_wpm, wpm, accuracy, date, time = line
        print(f'time taken: {time_taken}, wpm: {wpm}, accuracy: {accuracy}, date: {date}, time: {time}')