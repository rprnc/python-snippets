#Directed Graph question from Clem on youtube
#solved with strobly connected components to simplify the graph
#full solution not yet implemented in this file

airports = [
"BGI", "CDG", "DEL", "DOH", "DSM", "EWR", "EYW", "HND", "ICN",
"JFK", "LGA", "LHR", "ORD", "SAN", "SFO", "SIN", "TLV", "BUD"]

routes = [
["DSM", "ORD"], 
["ORD", "BGI"], 
["BGI", "LGA"], 
["SIN", "CDG"], 
["CDG", "SIN"], 
["CDG", "BUD"], 
["DEL", "DOH"], 
["DEL", "CDG"], 
["TLV", "DEL"], 
["EWR", "HND"], 
["HND", "ICN"], 
["HND", "JFK"], 
["ICN", "JFK"], 
["JFK", "LGA"], 
["EYW", "LHR"], 
["LHR", "SFO"], 
["SFO", "SAN"], 
["SFO", "DSM"], 
["SAN", "EYW"]]

#Starting Airport is LGA
#How many airports do we need to link to from LGA such that all airports are visitable



#using list comprehension make a routes to list and a routes from list
# for each airport in the airports list
# if it has no route to it then add it to the output list as we need to link to there from our start
# elif that airport is in the routes to list
# add it to a visited list
# check the airport in the routes from column as long as it isnt visited already, if it is visited then add the airport to the output
# 
# once visited  == airports
#return the length on output






def linkto(airports, routes):
    into = [i[1] for i in routes]
    outof = [i[0] for i in routes]
    output = [i in airports not in into]
    visited = []

    for i in into:
        visited.append(i)
        if outof[i] in visited:
            output.append(i) 
    return output