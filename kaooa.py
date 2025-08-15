import turtle

centers = []
circle_indexing = {1:3,2:1,3:4,4:2,5:5,6:6,7:7,8:8,9:9,10:10}
possible_moves = {1:[[6,7],[10,8]],2:[[7,8],[6,9]],3:[[8,9],[7,10]],4:[[9,10],[8,6]],5:[[6,10],[7,9]],6:[[7,10,5,1],[2,4]],7:[[6,8,1,2],[5,3]],8:[[7,9,2,3],[1,4]],9:[[8,10,3,4],[2,5]],10:[[6,9,4,5],[1,3]]}   # first 2 are immediate pos and next 2 are extreme(corner positions) so for jump only check first 2
crow_positions = []
cur_vulture_index = -1
killed = 0
total_crows = 7
crows_landed = 0
radius = 50
whose_turn = 's'
new_center_for_double_click = []
old_center_for_double_click = []

class Board:
    def __init__(self,size,radius):
        self.screen = turtle.Screen()
        self.screen.title("Kaooa Board")
        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()
        turtle.bgcolor("black")
        self.turtle.penup()
        self.turtle.goto(-600,100)
        self.turtle.pendown()
        self.turtle.speed(20)
        self.turtle.pensize(10)
        self.turtle.pencolor("white")
        self.size = size
        self.radius = radius

    def draw_star(self):
        for _ in range(5):
            self.turtle.forward(self.size)
            x, y = self.turtle.position()
            centers.append((x,y))
            self.turtle.right(144)

    def draw_circles(self):
        for i in range(0,5):
            center_x = centers[i][0]
            center_y = centers[i][1]
            self.turtle.penup()
            self.turtle.goto(center_x,center_y-self.radius)
            self.turtle.pendown()
            self.fill_the_circle(centers[i],"black")
        self.turtle.penup()
        self.turtle.goto(centers[4][0],centers[4][1])
        self.turtle.pendown() 
    
    def set_turtle_pos(self,forward,left,right):
        self.turtle.penup()
        self.turtle.right(right)
        self.turtle.forward(forward)
        self.turtle.left(left)
        x,y = self.turtle.position()
        centers.append((x,y))
        self.turtle.goto(x,y-self.radius)         # direction +ve x-axis
        self.turtle.pendown()
        self.fill_the_circle((x,y),"black")
        self.turtle.penup()
        self.turtle.goto(x,y)
    
    def draw_inner_circles(self):
        self.turtle.penup()
        self.turtle.goto(centers[4][0],centers[4][1])
        self.set_turtle_pos(465,0,0)      
        self.set_turtle_pos(280,0,0)      
        self.set_turtle_pos(280,73,73)   
        self.set_turtle_pos(280,143,143)      
        self.set_turtle_pos(285,216,216)

    def fill_the_circle(self,center,color):
        c_x = center[0]
        c_y = center[1]
        self.turtle.penup()
        self.turtle.goto(c_x, c_y - self.radius)
        self.turtle.pendown()
        self.turtle.begin_fill()
        self.turtle.fillcolor(color)
        self.turtle.circle(self.radius)
        self.turtle.end_fill()

    def clear_circle(self,center):
        c_x = center[0]
        c_y = center[1]
        self.turtle.penup()
        self.turtle.goto(c_x, c_y - self.radius)
        self.turtle.pendown()
        self.turtle.begin_fill()
        self.turtle.fillcolor("black")
        self.turtle.circle(self.radius)
        self.turtle.end_fill()

    def find_circle_index(self,pos):
        x = pos[0]
        y = pos[1]
        for center_test in centers:
            c_x = center_test[0]
            c_y = center_test[1]
            distance = ((x - c_x) ** 2 + (y - c_y) ** 2) ** 0.5
            if distance<=radius:
                center = center_test
                break

        for i in range(0,10):
            if centers[i]==center:
                new_unmapped = i+1
                break
        
        for ind in range(1,11):
            if circle_indexing[ind] == new_unmapped:
                new = ind
                break
        return new
    
    def write_message(self,message):
        self.turtle.penup()
        self.turtle.goto(0, 600)
        self.turtle.color("white")
        self.turtle.write(message, align="center", font=("Arial", 16, "normal"))
        turtle.ontimer(self.clear_message, 500)
    
    def clear_message(self):
        self.turtle.undo()

    def declare_results(self,message):
        self.turtle.penup()
        self.turtle.goto(0, -100)
        self.turtle.color("pink")
        self.turtle.write(message, align="center", font=("Arial", 30, "normal"))
        turtle.ontimer(self.clear_message, 1000)
    
class Crow:
    def __init__(self,board):
        self.board = board

    def place_crow(self,center):
        global crow_positions,whose_turn
        new_pos = self.board.find_circle_index(center)
        if new_pos in crow_positions:
            self.board.write_message("Invalid move: Crow is already present")
            whose_turn = 'c'
        else:
            self.board.fill_the_circle(center,"green")
            crow_positions.append(new_pos)
            whose_turn = 'v'

    def play_crow(self,old_c,new_c):
        global crow_positions,whose_turn
        new = self.board.find_circle_index(new_c)
        old = self.board.find_circle_index(old_c)
        if new in possible_moves[old][0] and new not in crow_positions and new != cur_vulture_index:
            self.board.clear_circle(old_c)
            crow_positions.remove(old)
            self.place_crow(new_c)
            whose_turn = 'v'
        else:
            if new not in possible_moves[old][0]:
                kaooa_board.write_message("Invalid move: Crow can go only to adjacent cells")
            if new in crow_positions:
                kaooa_board.write_message("Invalid move: Crow already present in that position")
            if new == cur_vulture_index:
                kaooa_board.write_message("Invalid move: Vulture is present. Crow cannot go there")
            whose_turn = 'c'

    def crows_win(self):
        global cur_vulture_index
        for test in possible_moves[cur_vulture_index][0]:
            if test not in crow_positions:
                return False
        
        for test2 in possible_moves[cur_vulture_index][1]:
            if test2 not in crow_positions:
                return False
        return True


class Vulture:
    def __init__(self,board):
        self.board = board

    def place_vulture(self,center):
        global cur_vulture_index
        self.board.fill_the_circle(center,"red")
        cur_vulture_index = self.board.find_circle_index(center)

    def capture_possible(self):
        global cur_vulture_index
        number_of_adj_places = len(possible_moves[cur_vulture_index][0])
        for i in range(number_of_adj_places):
            if possible_moves[cur_vulture_index][0][i] in crow_positions and i<len(possible_moves[cur_vulture_index][1]) and possible_moves[cur_vulture_index][1][i] not in crow_positions:
                return True
        return False

    def play_vulture(self,center):
        global cur_vulture_index, total_crows, crow_positions,whose_turn, killed
        new = self.board.find_circle_index(center)

        if cur_vulture_index==-1:
            self.place_vulture(center)
            whose_turn = 'c'
        
        elif self.capture_possible() == True and new not in possible_moves[cur_vulture_index][1]:
            kaooa_board.write_message("Invalid move: Vulture has to capture the crow")
            whose_turn = 'v'

        else:
            if new in possible_moves[cur_vulture_index][0] and new not in crow_positions: #adjacent
                self.board.clear_circle(centers[circle_indexing[cur_vulture_index]-1])
                self.place_vulture(center)  
                whose_turn = 'c'

            # double jump check
            elif new in possible_moves[cur_vulture_index][1] and new not in crow_positions: #valid double jump
                if new == possible_moves[cur_vulture_index][1][0]:
                    crow_to_kill = possible_moves[cur_vulture_index][0][0]
                else:
                    crow_to_kill = possible_moves[cur_vulture_index][0][1]

                if crow_to_kill in crow_positions: 
                        dead_crow_center = centers[circle_indexing[crow_to_kill]-1]  
                        vulture_center = centers[circle_indexing[cur_vulture_index]-1]               
                        self.board.clear_circle(dead_crow_center)
                        crow_positions.remove(crow_to_kill)
                        total_crows -= 1
                        killed += 1
                        self.board.clear_circle(vulture_center)
                        self.place_vulture(center)
                        kaooa_board.write_message(f"Crow died:( {total_crows} crows left!")
                        whose_turn = 'c'
                else:                       # crow not present
                    kaooa_board.write_message("Invalid move: Vulture can jump cell only if crow is present")
                    whose_turn = 'v'
            else:
                kaooa_board.write_message("Invalid move: Either move is not possible or cell is not free")
                whose_turn = 'v'


    def vultures_win(self):
        if killed >= 4:
            return True
           
def valid_click(crow,vulture,x,y):
    global new_center_for_double_click, old_center_for_double_click, whose_turn, crows_landed
    for center in centers:
        c_x = center[0]
        c_y = center[1]
        distance = ((x - c_x) ** 2 + (y - c_y) ** 2) ** 0.5
        if distance<=radius:
            if whose_turn == 's':
                crow.place_crow(center)
                crows_landed += 1
                whose_turn = 'v'
            elif whose_turn == 'v':
                vulture.play_vulture(center)

            elif whose_turn == 'c':
                if crows_landed < 7:
                    crow.place_crow(center)
                    crows_landed += 1

                else:
                    if len(old_center_for_double_click)==0:
                        old_center_for_double_click.append(center)
                        whose_turn = 'c'
                    else:
                        new_center_for_double_click.append(center)
                        crow.play_crow(old_center_for_double_click[0],new_center_for_double_click[0])
                        old_center_for_double_click.pop(0)
                        new_center_for_double_click.pop(0)
   
    if cur_vulture_index!=-1:
        if crow.crows_win():
            kaooa_board.declare_results("Crows win!!")
            turtle.exitonclick()

        elif vulture.vultures_win():
            kaooa_board.declare_results("Vultures win!")
            turtle.exitonclick()

def handle_click(x, y):
        valid_click(crow,vulture,x, y)
      
if __name__ == "__main__":
    kaooa_board = Board(1200,50)
    kaooa_board.draw_star()
    kaooa_board.draw_circles()
    kaooa_board.draw_inner_circles()

    crow = Crow(kaooa_board)
    vulture = Vulture(kaooa_board)

    kaooa_board.write_message("Welcome to KAOOA game!")
    turtle.Screen().onscreenclick(handle_click)

    turtle.mainloop()   