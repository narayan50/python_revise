# importing stastics modules

import statistics as st

l1 = [23, 34, 556, 7678, 343]

print("mean of the l1 list :---" ,st.mean(l1))


# median modules not only perform the operation but also sort the data internally

t1= (23,3,5,23,20,45,12)

# no needed just to display
t2=(sorted(t1))
print(t2)

print("medain of t2 is:---",st.median(t2))

# findint a modes what is most frequent repeated datas

t4=(23,23,34,3,21,34,5,22,1,1,3,3,1,8)
print("mode of the l1 list is :----", st.mode(t4))

# min  max
t5=(23,34,34,5,12,35,12,45,56,56,422)

print("min of t5 is :--------",min(t5))
print("max of t5 is :--------",max(t5))

# varianvce
# standard deviation
# geomatric mean
# quartiels
# correlations




