

def main():

    def check_square(row,col):
        row_floor = row//3
        col_floor = col//3
        print(row_floor)
        print (col_floor)
        for i in range(0,3):
            print("i: "+str(i))
            for j in range(0,3):
                #reverse again? spaghetti code moar plz
                #reversing it didnt fix it...so maybe macaroni code?
                print ("j: "+str(j))
                print("RF+i: " +str(row_floor*3+i))
                print("RC+j: "+str(col_floor*3+j))
        return False

    #check_square(6,8)

    def check_break():
        x = 0
        while x < 10:
            x+=1
            if x > 5:
                print("break?")
                continue
            print("no break?")

    check_break()
if __name__ == "__main__":
    main()