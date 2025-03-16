def tisec(seconds):
    hours=seconds//3600
    minutes=(seconds%3600)//60
    seconds=seconds%60
    return f"{hours:02}:{minutes:02}:{seconds:02}"
tiseconds = int(input("Enter time in seconds: "))
print("Time in HH:MM:SS format:", tisec(tiseconds))
