
gridlen = 100

insts = '<>v^[].,+-'

class programme:
    def __init__(self,code:str):
        self.grid = [[0 for x in range(gridlen)] for y in range(gridlen)]
        self.px,self.py=0,0
        self.cursor = 0
        self.code=code
        self.end=False
    def update(self):
        current = self.code[self.cursor]

        if current == '>':
            self.px+=1
            if self.px>=gridlen:
                print(f'position error : grid cursor to high in x position (>={gridlen})')
                self.end = True
        elif current == '<':
            self.px-=1
            if self.px<0:
                print(f'position error : grid cursor to low in x position (<0)')
                self.end=True
        if current == '^':
            self.py+=1
            if self.py>=gridlen:
                print(f'position error : grid cursor to high in x position (>={gridlen})')
                self.end = True
        elif current == 'v':
            self.py-=1
            if self.py<0:
                print(f'position error : grid cursor to low in x position (<0)')
                self.end=True
        elif current == '+':
            self.grid[self.px][self.py]+=1
        elif current == '-':
            self.grid[self.px][self.py]-=1
        elif current == '.':
            print(chr(self.grid[self.px][self.py]))
        elif current == ',':
            self.grid[self.px][self.py] = ord(input())
        elif current=='[':
            if self.grid[self.px][self.py]==0:
                while self.code[self.cursor] != ']':
                    
                    self.cursor+=1
                    if self.cursor==len(self.code)-1:
                        print('unexpeted EOF expected ]')
                        self.end=True
                        break
        elif current==']':
            while self.code[self.cursor+1]!='[':
                self.cursor-=1
                


        self.cursor+=1

        if self.cursor>=len(self.code):self.end=True

        

def start(code:str):
    thread = programme(code)
    while not thread.end:
        thread.update()
