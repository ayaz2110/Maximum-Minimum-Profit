from tkinter import *
import random

root = Tk()
root.title("Maximum/Minimum Profit")
root.geometry("500x500")

month = ("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec")

profits = (1,2,3,4,5,6,7,8,9,10,11,12)

max_profit = max(profits)
max_profit_index = profits.index(max_profit)
print(max_profit_index)

max_profit_month = month[max_profit_index]
print("The Maximum Profit Of " + str(max_profit) + "Was Recorded On The Month Of " + str(max_profit_month))

min_profit = min(profits)
min_profit_index = profits.index(min_profit)
print(min_profit_index)

min_profit_month = month[min_profit_index]
print("The Minimum Profit Of " + str(min_profit) + "Was Recorded In The Month Of " + str(min_profit_month))

root.mainloop()
