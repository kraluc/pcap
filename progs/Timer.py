class Timer:
    def __init__(self, hours: int = 0, minutes: int = 0, seconds: int = 0):
        seconds = int(seconds)
        minutes = int(minutes) + seconds // 60
        hours = int(hours) + minutes // 60

        self.__hours = hours % 24
        self.__minutes = minutes % 60
        self.__seconds = seconds % 60

    def __str__(self):
        template = "{:0>2d}:{:0>2d}:{:0>2d}"
        return template.format(self.__hours, self.__minutes, self.__seconds)

    def next_second(self):
        seconds = self.__seconds + 1
        minutes = self.__minutes + seconds // 60
        hours = self.__hours + minutes // 60

        self.__seconds = seconds % 60
        self.__minutes = minutes % 60
        self.__hours = hours % 24

    def prev_second(self):
        seconds = self.__seconds - 1
        minutes = self.__minutes + seconds // 60
        hours = self.__hours + minutes // 60

        self.__seconds = seconds % 60
        self.__minutes = minutes % 60
        self.__hours = hours % 24


timer = Timer(23, 59, 59)
print(timer)

timer.next_second()
print(timer)

timer.prev_second()
print(timer)
