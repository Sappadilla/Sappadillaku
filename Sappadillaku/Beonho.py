import random

class Beonho (object):

    def __init__(self):

        #initialize list of rows with 0z, equaling blanks bb
        self.beonhodo = []
        for i in range(0,9):
            self.beonhodo.append([])
            for j in range(0,9):
                self.beonhodo[i].append(0)

        #intialize board with values huuun
        #LOL THIS IS SO INEFFICIENT
        #I THINK THIS IS EXPONENTIAL LMAO
        self.count = 0
        self.bad_count = 0 #acts as our cheap limiter, else infinite loop

        x = 0
        #getting closer, just gets stuck when one spot open in a row
        # - reason it's getting stuck is there is only one option that doesn't fit in the one spot left.  FUCK
        # - need to go back to the drawing board and really analyze what properties the board has
        #need to make y range modular
        #use random.choice(list)
        # y_list = [0,1,2,3,4,5,6,7,8]
        # num_list = [1,2,3,4,5,6,7,8,9]
        # while self.count <= 80 and self.bad_count <=100000:
        #     if self.check_full("row",x):
        #         if x//3 < 2:
        #             x+=3
        #             y_list =[0,1,2,3,4,5,6,7,8]
        #             num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        #             continue
        #         elif x%3 < 2:
        #             x = x%3+1
        #             y_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        #             num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        #             continue
        #         else: break
        #
        #     num = random.choice(num_list)
        #     y = random.choice(y_list)
        #     if (self.check_col(num,y) or self.check_square(num,x,y)) and len(y_list) < 2 :
        #         self.zeroize_row(x)
        #         y_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        #         num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        #         self.bad_count += 1
        #         print("huh?")
        #         self.count -= 8
        #         continue
        #     #this is starting to look like recursion, might be a much more effective solution
        #     if len(y_list) == 2:
        #         if (self.check_col(num,y_list[0]) or self.check_square(num,x,y_list[0])) and \
        #                 (self.check_col(num,y_list[1]) or self.check_square(num,x,y_list[1])):
        #
        #             self.zeroize_row(x)
        #             y_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        #             num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        #             self.bad_count += 1
        #             print("huh2?")
        #             self.count -=7
        #             continue
        #     if len(y_list)==3:
        #         if (self.check_col(num, y_list[0]) or self.check_square(num, x, y_list[0])) and \
        #                 (self.check_col(num, y_list[1]) or self.check_square(num, x, y_list[1])) and \
        #                 (self.check_col(num, y_list[2]) or self.check_square(num, x, y_list[2])):
        #
        #             self.zeroize_row(x)
        #             y_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        #             num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        #             self.bad_count += 1
        #             print("huh3?")
        #             self.count -= 6
        #             continue
        #
        #     if self.check_all(num,x,y):
        #         self.bad_count+=1
        #         continue
        #     self.beonhodo[x][y] = num
        #     self.count+=1
        #     y_list.remove(y)
        #     num_list.remove(num)
        #     print(self.count)
        #     #print("y len: "+str(len(y_list)))


        # while self.count <= 45 and self.bad_count <= 100000:
        #     num = random.randrange(1, 10)
        #     x = random.randrange(0,9)
        #     if self.check_row(num,x):
        #         self.bad_count += 1
        #         continue
        #     y = random.randrange(0,9)
        #     if self.check_occupied(x,y):
        #         self.bad_count += 1
        #         continue
        #     if self.check_col(num,y):
        #         self.bad_count += 1
        #         continue
        #     if self.check_square(num,x,y):
        #         self.bad_count += 1
        #         continue
        #     self.beonhodo[x][y] = num
        #     self.count+=1
        #     print("good count: "+str(self.count))


        #this constructor attempt goes number by number instead of row by row
        self.current = 1
        self.rows = [0,1,2,3,4,5,6,7,8]
        self.cols = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        while self.current <= 9 and self.bad_count <= 10000:
            r = random.choice(self.rows)
            c = random.choice(self.cols)
            if self.check_occupied(r,c):
                self.bad_count +=1
                continue
            elif self.check_all(self.current,r,c):
                self.bad_count +=1
                continue
            else:
                self.beonhodo[r][c] = self.current
                self.rows.remove(r)
                self.cols.remove(c)
                if len(self.rows) == 0:
                    self.current +=1
                    self.rows = [0, 1, 2, 3, 4, 5, 6, 7, 8]
                    self.cols = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    def __getitem__(self,item):
        return self.beonhodo[item]

    def __setitem__(self,item,key):
        self.beonhodo[key] = item

    def check_row(self,num,row):
        for i in range(0,9):
            if self.beonhodo[row][i] == num:
                return True
        return False

    def check_full(self,what,index):
        for i in range(0,9):
            if self.beonhodo[index][i] == 0:
                return False
        return True

    def zeroize_row(self,row):
        for i in range(0,9):
            self.beonhodo[row][i] = 0


    def check_col(self,num,col):
        for i in range(0,9):
            if self.beonhodo[i][col] == num:
                return True
        return False

    def check_square(self,num,row,col):
        row_floor = row//3
        col_floor = col//3
        for i in range(0,3):
            for j in range(0,3):
                if self.beonhodo[row_floor*3+i][col_floor*3+j] == num:
                    return True
        return False

    def check_occupied(self,row,col):
        return self.beonhodo[row][col] != 0

    def check_all(self,num,row,col):
        return self.check_row(num, row) or \
               self.check_col(num, col) or \
               self.check_square(num,row,col) or \
               self.check_occupied(row,col)