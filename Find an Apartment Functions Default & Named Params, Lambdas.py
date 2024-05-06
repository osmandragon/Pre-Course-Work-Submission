#def apt_search1(city, max_rent, min_beds, pets_allowed):
#if pets_allowed == "yes":
  #print("Welcome to GC Property Management! Looking up listings in " ,city, " for " ,min_beds, " bedrooms apartments that allow pets, all within a budget of " ,max_rent, " per month'...")
 #else:
  #print("Welcome to GC Property Management! Looking up listings in " ,city, " for " ,min_beds, " bedrooms apartments that do not allow pets, all within a budget of " ,max_rent, " per month'...")
#apt_search1("New York" , "$2000" , 2 , "yes")
#apt_search1("texas" , "$7000" , 1 , "no")
def apt_search2(city, max_rent, min_beds = 1, pets_allowed = "yes"):
    if pets_allowed == "yes":
        print("Welcome to GC Property Management! Looking up listings in " ,city, " for " ,min_beds, " bedrooms apartments that allow pets, all within a budget of " ,max_rent, " per month'...")
    else:
        print("Welcome to GC Property Management! Looking up listings in " ,city, " for " ,min_beds, " bedrooms apartments that do not allow pets, all within a budget of " ,max_rent, " per month'...")
apt_search2("New York" , "$2000" , 2 , "yes")
apt_search2("texas" , "$7000" , 1)
apt_search2("New York" , "$2000" , "yes")
#plus_one_hundred
#x = lambda a: a + 100
#print(x(5))

#square_num
#x = lambda a: a * 2
#print(x(5))

#concatenate
#x = lambda a: a +
#print(x(5))
