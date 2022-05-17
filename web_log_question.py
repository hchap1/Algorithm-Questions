#Web Log exmaple. (I've no idea how the timestamp actually works, so I just did hour:minute:second:milisecond).
web_log = [
    ["Jack", "5:13:45:200", "youtube.com"],
    ["Jack", "6:43:13:100", "amazon.com"],
    ["Bob", "12:32:59:900", "amazon.com"],
    ["Bob", "12:04:13:400", "youtube.com"],
    ["Jack", "12:40:16:500", "github.com"],
    ["Bob", "11:45:42:400", "scratch.mit.edu"],
    ["Chris", "15:52:02:000", "youtube.com"],
    ["Chris", "16:00:45:090", "google.com"]
    ]

#Record the times to order them.
times = []

for log in web_log:
    time = int("".join(log[1].split(":")))
    times.append(time)

#Orders times.
times.sort()
print(times)

new_web_log = []
for i in range(len(web_log)):
    new_web_log.append([])

#Basically, for each item in the log, it find the index of it's time in times, and places it at the same index in the sorted web log. 
for name, time, place in web_log:
    new_web_log[times.index(int("".join(time.split(":"))))] = [name, time, place]

#Initializes variable for the actual finding of paths.
web_log = new_web_log
paths = {}
transitions = []

for name, time, place in web_log:
    if name not in paths.keys():
        paths[name] = place
    else:
        paths[name] += ", " + place

for person in paths:
    if len(paths[person].split(", ")) == 2:
        transitions.append(paths[person].split(", "))
    elif len(paths[person].split(", ")) > 2:
        this_path = paths[person].split(", ")
        for page in range(len(this_path)):
            if page == len(this_path)-1:
                pass
            else:
                #Adds the website, and then the one after it (to get the transition).
                transitions.append([this_path[page], this_path[page+1]])
best = ["NAN",0]
for transition in transitions:
    #Finds most common transition.
    if transitions.count(transition) > best[1]:
        best = [transition, transitions.count(transition)]
transition, count = best
#Outputs most common transition.
print("Most common transition is %s, with %s occurences." % (transition[0] + " -> " + transition[1], count))
    
    
        
    
