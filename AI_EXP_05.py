import math
def alpha_beta(depth,nodeIndex,maximizingPlayer,values,alpha,beta,height):
    if depth==height:


        return values[nodeIndex]
    if maximizingPlayer:
      best =-math.inf
      for i in range(2):
        value=alpha_beta(
            depth+1,nodeIndex*2+i,False,values,alpha,beta,height

        )
        best=max(best,value)
        alpha = max(alpha,best)

        if beta<=alpha:
          break
      return best
    else:
      best=math.inf
      for i in range(2):
        value= alpha_beta(depth+1,nodeIndex*2+i,True,values,alpha,beta,height)
        best=min(best,value)
        beta=min(beta,best)
        if beta<=alpha:
          break
      return best

values=list(map(int,input().split()))
height=3
print("\noptimal value" ,alpha_beta(0,0,True,values,-math.inf,math.inf,height))


#output

"""
3 5 6 9 1 2 0 -1 

optimal value 5


"""