import csv

#configuration
csvfilePath=".\slr_dm_1.csv"
neededColumnnames=["survey", "dm","topdown","data"]


def get_transposed_csv():
    #table= pn.DataFrame
    with open(csvfilePath) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        skip=True
        dict={}
        for row in spamreader:
            if skip:
                skip=False
                #continue
            dict[row[0]]=row[1:]
            
    columns= dict.keys
    
    searchstring=""
    for col in neededColumnnames:
        strPart="("
        colList=dict[col]
        for term in colList:
            #if not pn.isna(term):
            if term=='':
                continue
            strPart+='"'+ term + '"' + " OR "
        strPart= strPart.rsplit(' ', 2)[0]
        strPart+=") AND "
        searchstring+=strPart
    searchstring= searchstring.rsplit(' ', 2)[0]
    return searchstring
    


print()
print(get_transposed_csv())