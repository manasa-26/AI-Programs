from collections import defaultdict
visited=defaultdict(lambda:False)
J1,J2,L=0,0,0
def Water_Jug_Problem(X,Y):
  global J1,J2,Litre
  if(X==L and Y==0)or(Y==L and X==0):
    print("(",X,",",Y,")",sep="")
    return True
  if visited[(X,Y)]==False:
    print("(",X,",",Y,")",sep="")
    visited[(X,Y)]=True
    return(Water_Jug_Problem(0,Y) or Water_Jug_Problem(X,0) or
    Water_Jug_Problem(J1,Y) or Water_Jug_Problem(X,J2) or
    Water_Jug_Problem(X+min(Y,(J1-X)),Y-min(Y,(J1-X))) or Water_Jug_Problem(X-min(X,(J2-
    Y)),Y+min(X,(J2-Y))))
  else:
    return False

J1=4
J2=3
L=2
print("Path is as follows")
Water_Jug_Problem(0,0)
