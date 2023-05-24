def menuMaker():
    #box below: horiz, vert, TL corner, TR corner, BL corner, BR corner, Right Pointing T, LP T, DP T, UP T, cross
    Box = ['\U00002550','\U00002551' ,'\U00002554', '\U00002557','\U0000255A', '\U0000255D','\U00002560', '\U00002563','\U00002566', '\U00002569','\U0000256C','\U00002550'*75]
    options = []
    while True:
        count =0
        Mwidth = 0
        ans = (input("option item:"))
        if ans != "DONEXYZ":
            options.append(ans)
            
            for i in options:
                
                if Mwidth < len(i):
                    Mwidth = len(i)
            if count ==0:
                print(Box[2]+Box[0]*Mwidth+Box[3])
                print(Box[1]+options[count].center(Mwidth)+Box[1])
                count+=1
            while count < len(options)-1:
                print(Box[6]+Box[0]*Mwidth+Box[7])
                print(Box[1]+options[count].center(Mwidth)+Box[1])
                count+=1
            while count < len(options):
                print(Box[6]+Box[0]*Mwidth+Box[7])
                print(Box[1]+options[count].center(Mwidth)+Box[1])
                print(Box[4]+Box[0]*Mwidth+Box[5])
                count+=1
            count +=1
        else:
            borderStyle = input("1 = \U0000256C \n2 = \U0000254B\n3 = \U0000253C\n") 
            options.insert(0,r'options = ["'+options[0])
            options.reverse()
            options.insert(0,options[0]+r'"]')
            options.reverse()
            print(r"Box = ['\U00002550','\U00002551' ,'\U00002554', '\U00002557','\U0000255A', '\U0000255D','\U00002560', '\U00002563','\U00002566', '\U00002569','\U0000256C','\U00002550'*75]")
            print(r"#Box: horiz, vert, TL corner, TR corner, BL corner, BR corner, Right Pointing T, LP T, DP T, UP T, cross")
            print(*options, sep = r'", "')
            for i in options:
                Mwidth = 0
                if Mwidth < len(i):
                    Mwidth = len(i)+1
            if count ==0:
                print(r"print(Box[2]+Box[0]*"+str(Mwidth)+r"+Box[3])")
                print(r"print(Box[1]+options["+str(count)+r"].center("+str(Mwidth)+r")+Box[1])")
                count+=1
            while count < len(options)-1:
                print(r"print(Box[6]+Box[0]*"+str(Mwidth)+r"+Box[7])")
                print(r"print(Box[1]+options["+str(count)+r"].center("+str(Mwidth)+r")+Box[1])")
                count+=1
            while count < len(options):
                print(r"print(Box[6]+Box[0]*"+str(Mwidth)+r"+Box[7])")
                print(r"print(Box[1]+options["+str(count)+r"].center("+str(Mwidth)+r")+Box[1])")
                print(r"print(Box[4]+Box[0]*"+str(Mwidth)+r"+Box[5])")
                print("\n\n\n")
                count+=1            

menuMaker()


