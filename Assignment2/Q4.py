#Consider the following two sets, A and B, represenƟng scores of two teams in mulƟple
#matches. A = {34, 56, 78, 90} and B = {78, 45, 90, 23}
#WAP to perform the following operaƟons using set funcƟons:
#i. Find the unique scores achieved by both teams (union of sets).
#ii. IdenƟfy the scores that are common to both teams (intersecƟon of sets).
#iii. Find the scores that are exclusive to each team (symmetric difference).
#iv. Check if the scores of team A are a subset of team B, and if team B's scores are
#a superset of team A.
#v. Remove a specific score X (input by the user) from set A if it exists. If not, print
#a message saying it is not present.

A = {34, 56, 78, 90}
B = {78, 45, 90, 23}

# i. Find the unique scores achieved by both teams (union of sets).
union= A.union(B)
print("unique scores:", union)

# ii. IdenƟfy the scores that are common to both teams (intersecƟon of sets).
intersection = A.intersection(B)
print(" common scores:", intersection)

# iii. Find the scores that are exclusive to each team (symmetric difference).
exclusivescores = A.symmetric_difference(B)
print(" exclusive scores:", exclusivescores)

# iv.Check if the scores of team A are a subset of team B, and if team B's scores are
#a superset of team A.
Asubset = A.issubset(B)
Bsuperset = B.issuperset(A)
print(" scores of team A are a subset of team B", Asubset)
print("team B's scores are a superset of team A.", Bsuperset)

#v. Remove a specific score X (input by the user) from set A if it exists. If not, print
#a message saying it is not presen
X = int(input("Enter a score to remove from team A: "))
if X in A:
    A.remove(X)
else:
    print(f"Score {X} is not present")
    
print(A)  

