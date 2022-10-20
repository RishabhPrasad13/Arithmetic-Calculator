

def arithmetic_arranger(problems,solve=False): #optional parameter solve must have a default value. it is false unless specified
    top=''
    middle=''
    line=''
    bottom=''
    answers=''

    for q in problems:
        char=q.split(' ')
        big_num=len(max(char,key=len))
        dash_num= big_num+2
        space= dash_num-len(char[2])-1
        dash = '-' * dash_num

        if '*'in char or '/' in char:
            return 'Error: unrecognized operators' #return kills the loop immediatly

        if char[1] == '+':
            sumint=int(char[0])+int(char[2])
            line2 = ('+' + ' ' * space + char[2])

        elif char[1] == '-':
            sumint = int(char[0]) - int(char[2])
            line2 = ('-' + ' ' * space + char[2])

        sumstr=str(sumint)
        line1=(char[0])



        top+=line1.rjust(8)+' '*4
        middle+=line2.rjust(8)+' '*4
        line+=dash.rjust(8)+' '*4
        bottom+=sumstr.rjust(8)+' '*4
        answers+=sumstr.rjust(8)+' '*4

    if solve is True:
        arranged = top+'\n' + middle+'\n' + line+'\n' + answers


    else:
        arranged=top+'\n' + middle+'\n' + line

    return arranged





