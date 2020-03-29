#It's New Year's Day and everyone's in line for the Wonderland rollercoaster ride! 
#There are a number of people queued up, and each person wears a sticker indicating their initial position in the queue. 
#Initial positions increment by 1 from 1 at the front of the line to n at the back.

#Print an integer denoting the minimum number of bribes needed to get the queue into its final state. 
#Print Too chaotic if the state is invalid, i.e. it requires a person to have bribed more than 2 people.

#!!! Person can bribe only with the person in front of him/her 


def minimumBribes(q):
    moves = 0 
    q = [P-1 for P in q]
    for i,P in enumerate(q):
        if P - i > 2:
            print("Too chaotic")
            return
        for j in range(max(P-1,0),i):
              if q[j] > P:
                moves += 1
    print(moves)



minimumBribes([1,2,5,3,7,8,6,4])