profile={
    'name':'raju',
    'age':100,
    'salary':300000,
    
}
# get() : retrive the data of specific key
age = profile.get('age','Not Found')
print(age)