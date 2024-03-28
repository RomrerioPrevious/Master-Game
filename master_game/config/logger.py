import datetime


class Logger:
    @staticmethod
    def info() -> str:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        return f"{time} info | "

    @staticmethod
    def error() -> str:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        return f"{time} error | "

    @staticmethod
    def custom(debug: str):
        time = datetime.datetime.now().strftime("%H:%M:%S")
        return f"{time} {debug} | "

    @staticmethod
    def write_log(log: str):
        with open("logs.log", "w", encoding="UTF-8") as file:
            file.write(log)