import time
my_time = int(input("Enter the time in seconds (greater than 0): "))
for x in range(my_time,0,-1):
    seconds = x % 60    
    minutes = (x // 60) % 60
    hours = (x // 3600) % 24
    print(f"{hours:02}:{minutes:02}:{seconds:02} remaining")
    time.sleep(1)
    print("Time is up!")