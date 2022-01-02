# import matplotlib
# from datetime import datetime
# import datetime as dt
# from matplotlib import pyplot as plt
from hdn import Parser
import sys
'''
format in which progress data is stored:
    time_taken, raw_wpm, wpm, accuracy, date, time

'''
try:
    command = sys.argv[1]
except IndexError:
    command = None

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

    # def plot(self):
    #     lines = self.show_progress_text()
    #     times_taken = []
    #     raw_wpms = []
    #     wpms = []
    #     accuracies = []
    #     dates = []
    #     times = []
    #     for line in lines:
    #         time_taken, raw_wpm, wpm, accuracy, date, time = line
    #         times_taken.append(time_taken)
    #         raw_wpms.append(raw_wpm)
    #         wpms.append(int(float(wpm)))
    #         accuracies.append(accuracy)
    #         dates.append(date)
    #         times.append(time)

    #     ax = plt.gca()
    #     x_values = [datetime.strptime(d,"%d/%m/%Y").date() for d in dates]
    #     y_values = wpms
    #     formatter = dt.mdates.DateFormatter("%Y-%m-%d")
    #     ax.xaxis.set_major_formatter(formatter)

    #     locator = datetime.mdates.DayLocator()

    #     ax.xaxis.set_major_locator(locator)

    #     plt.plot(x_values, y_values)

# if __name__ == '__main__':
#     tp = TrackPractice('progress.hdn')
#     tp.plot()
if command == 'show_progress':
    tp = TrackPractice('progress.hdn')
    lines = tp.show_progress_text()
    index = 0
    for line in lines:
        time_taken, raw_wpm, wpm, accuracy, date, time = line
        print(f'time taken: {time_taken}, wpm: {wpm}, accuracy: {accuracy}, date: {date}, time: {time}')
        index += 1
    print(f'number of times typing-practice used: {index}')

