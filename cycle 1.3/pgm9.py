y={'alen':4,'meghan':2,'kumar':1,'chiran':3}
l=list(y.items())
l.sort()
print("Ascending order: ",l)
l=list(y.items())
l.sort(reverse=True)
print("Descending order: ",l)
dict=dict(l)
print("Dictionary:",dict)




