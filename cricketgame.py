import random
import string

Team_A=[]
Team_B=[]
wicket=0
Team_A_final_runs=0
Team_B_final_runs=0

class players:
    number_of_players=22
    middle_index=number_of_players//2

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def name_generator(size=random.randint(5,9), chars=string.ascii_uppercase):
        ng=''.join(random.choice(chars) for i in range(size)) 
        return ng
        
    def age_generator():
        ag=random.randint(22,30)
        return ag

    def player_generator():
        all_players=[]
        for j in range(players.number_of_players):
            all_players.append(players(players.name_generator(),players.age_generator()))
        middle_index=players.number_of_players//2
        global Team_A
        Team_A= all_players[:middle_index]  
        global Team_B
        Team_B= all_players[middle_index:] 
        return Team_A,Team_B     

class Balls:
    def each_ball():
        ball=random.randrange(0,999,2)
        return Balls.last_digit(ball)

    def last_digit(n):
        n = str(n)
        for_one_ball=(2 if int(n[len(n)-1])==8 else int(n[len(n)-1]))
        return for_one_ball
         

class overs(Balls):
    balls_for_one_over=6    

    def each_over():
        runs_in_over=[]
        for _ in range(overs.balls_for_one_over):
            score=Balls.each_ball()
            print(score)
            if score==0:
                global wicket
                wicket+=1
                if wicket==11:
                    print('All the players in {} got OUT'.format('Team A' if Team_in_strike==Team_A else 'Team B'))                   
                    break
                print('Player {} got OUT'. format(Team_in_strike[wicket-1].name))
                if wicket==11:
                    break
                continue
            else:
                runs_in_over.append(score)
        return sum(runs_in_over)
                   
    def all_overs():
        total_runs=0
        for i in range(1,Total_over+1):
            total_runs += overs.each_over()
            if wicket==players.middle_index or Total_over==i-1:
                break
            print('At the end of {0} over {1} scored {2}'.format(i,'Team A' if Team_in_strike==Team_A else 'Team B',total_runs))
            print('{}/{} ({})'.format(total_runs,wicket,i))         
        if Team_in_strike==Team_A:
            global Team_A_final_runs
            Team_A_final_runs=total_runs  
        global Team_B_final_runs
        Team_B_final_runs=total_runs  

def find_the_winner():
    if Team_A_final_runs!=Team_B_final_runs:
        winner=lambda a,b: 'Team_A' if a>b else 'Team_B'
        w='***** WINNING TEAM OF THE MATCH IS {} *****'.format(winner(Team_A_final_runs,Team_B_final_runs))
        print(w)

players.player_generator()
print('*****Introduction******\n This program is for Book cricket there will be two teams,each team will have 11 players.\n In the book cricket, Book will be opend ones in reverse for one ball.\n By opening the book in revers we will get even page numbers\n The last digit of a page number is considered as a run for each ball.\n (0,2,4,6, and 8) 0 is consider as out and 8 is considered as 2.\n There will be 6 balls for one over the number of overs is given by the user in this program.')
print('    Team_A           Team_B\n Name       Age  Name      Age')
for i in range(players.middle_index):
    print((Team_A[i].name,Team_A[i].age),(Team_B[i].name,Team_B[i].age))
Total_over=int(input('Enter the total numbers of over:'))
for i in range(2):
    Team_in_strike=Team_A if i==0 else Team_B
    print('{} is batting'.format('Team A' if Team_in_strike==Team_A else 'Team B'))
    overs.all_overs()   
    print('TOTAL RUNS SCORED BY {} IS {}'.format('Team A' if Team_in_strike==Team_A else 'Team B',Team_A_final_runs if Team_in_strike==Team_A else Team_B_final_runs))
    if i==1:
        break
    input("Press Enter to start second innings.....")
    globals()['wicket']=0
find_the_winner()




    








   