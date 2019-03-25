datafile = open("dataexport.csv", "r")

output = ""
newWard = False
totalRegistered = 0
totalVoted = 0

for line in datafile:
    line = line[:-3]

    # we just set a new ward, so we don't need the table header data
    if newWard:
        newWard = False
        continue

    # if we find a new ward, we set a new ward

    elif line[0:4] == "WARD":
        newWard = True
        wardExplode = line.split(",", 1)
        wardExplode = wardExplode[0].split(" ")
        wardNumber = wardExplode[1]

    #  we have a new row
    else:
        precinctExplode = line.split(",")
        precinctNumber = precinctExplode[0]
        precinctRegistered = precinctExplode[1]
        precinctVoted = precinctExplode[2]

        if precinctNumber == 'Total' or precinctNumber == '':
            continue

    #     we add to the output
        output += wardNumber + "," + precinctNumber + "," + precinctRegistered + "," + precinctVoted + "\n"
        totalRegistered = totalRegistered + int(precinctRegistered)
        totalVoted = totalVoted + int(precinctVoted)

print("Total registered", totalRegistered)
print("Total voted", totalVoted)

o = open("precinctdata.csv", "w")
o.write(output)
o.close()

datafile.close()