file=open("find_even_lines_file.txt", mode='w+')
cricket_batting_order=["Rohit\n","Gill\n","Virat\n","Kl\n","Iyer\n","Hardik\n","MSD\n","Jaddu\n"]
file.writelines(cricket_batting_order)
file.close()
try:
    file = open("find_even_lines_file.txt", mode='r')
    file_even = file.readlines()
    for batters in range(len(file_even)):
        if batters % 2 == 0:
            print(file_even[batters])
except(ZeroDivisionError) as message:
    print("you are dividing with  0")

    file.close()