import itertools

#define jaccard similarity (size of intersection over size of union)
def jaccard_sim(list1, list2):
    intersection = len(list(set(list1).intersection(list2)))
    union = (len(list1) + len(list2)) - intersection
    return float(intersection) / union


def print_customers():
    for x in cust:
        print (x,":",cust[x])



def merge():
    sim={}
    print("Computing pair wise similarities")
    for pair in itertools.combinations(cust, r=2):
        s=jaccard_sim(cust[pair[0]],cust[pair[1]])
        print("Jaccard_sim of",*pair,' is ',s)
        sim[tuple([pair[0],pair[1]])]=s
    #find pair with max similarity
    best_pair=max(sim, key=sim.get)
    print("Best pair to merge is",best_pair)
    #new cluster contains union of customers
    new_user_purchases=set(cust[best_pair[0]]).union(cust[best_pair[1]])
    #remove individual users
    cust.pop(best_pair[0])
    cust.pop(best_pair[1])
    #add merged pair
    cust[best_pair[0]+'+'+best_pair[1]]=new_user_purchases

    
    
def HierarchicalClustering(k):
    while(len(cust)>k):
        print("================================")
        print("There are",len(cust),"clusters")
        print_customers()
        merge()
        
#define some toy customer purchases to play around
cust={
    'user1':['milk','bread','coffee'],
    'user2':['milk','bread','cola'],
    'user3':['cereal','milk','donut'],
    'user4':['donut','cream','cola'],
    'user5':['cola','milk','cereal','tea']
}
HierarchicalClustering(2)
print("================================")
print("Final Clusters:")
print_customers()
