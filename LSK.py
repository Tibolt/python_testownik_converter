import re 

filename = "LSK_2017_BAZA.txt"

file = open(filename, 'r', encoding="utf8")

correct = []
questions = []
answears = []
answears_all = []
curr_question = False
last_question = ""

def get_data():
    #get data from file
    for idx, line in enumerate(file):
        #check if line is X100
        if re.search("([X])\w+\d", line) != None:
            correct.append(line.split()[0])
            last_question = (next(file))
            questions.append(last_question)
            curr_question = True
        # check if blank line
        elif line.strip():
            if line not in questions and curr_question==True:
                answears.append(line)
        else:
            answears_all.append(tuple(answears))
            answears.clear()
            curr_question = False

def write_data():
    #write data to sperate files
    for i,x in enumerate(correct):
        try:
            #you need to create folder called baza
            #also on linux/mac change baza\ for baza/ bellow
            f = open(f"baza\{i}.txt", "a", encoding="utf8")
            f.write(f"{correct[i]}\n")
            f.write(questions[i])
            for a in answears_all[i]:
                f.write(a)
            f.close()
        except:
            print(f"Error on question: {i}, {x}")
            pass

get_data()
write_data()
    