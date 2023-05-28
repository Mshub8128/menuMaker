def menuMaker():
    #box below: horiz, vert, TL corner, TR corner, BL corner, BR corner, Right Pointing T, LP T, DP T, UP T, cross
    Box = [['\U00002550','\U00002551','\U00002554','\U00002557','\U0000255A','\U0000255D','\U00002560','\U00002563','\U00002566','\U00002569','\U0000256C'],['\U00002500','\U00002502','\U0000250C','\U00002510','\U00002514','\U00002518','\U0000251C','\U00002524','\U0000252C','\U00002534','\U0000253C']]
    #Style = int(input("1 = \U0000256C \n2 = \U0000253C\n"))-1 
    Style = 1
    options = []
    print("'MM:X' to finish, 'S:1' to select double border, 'S:2' to select single border")
    while True:
        line = len(options)+1

        count =0
        Mwidth = 0
        ans = (input("Menu Item "+str(line)+":"))
        if ans == "S:1":
            Style = 0
            print("Double Border Style")
        elif ans == "S:2":
            Style = 1
            print("Single Border Style")            
        elif ans != "MM:X":
            options.append(ans)
            
            for i in options:
                
                if Mwidth < len(i):
                    Mwidth = len(i)
            if count ==0:
                print(Box[Style][2]+Box[Style][0]*Mwidth+Box[Style][3])
                print(Box[Style][1]+options[count].center(Mwidth)+Box[Style][1])
                count+=1
            while count < len(options)-1:
                print(Box[Style][6]+Box[Style][0]*Mwidth+Box[Style][7])
                print(Box[Style][1]+options[count].center(Mwidth)+Box[Style][1])
                count+=1
            while count < len(options):
                print(Box[Style][6]+Box[Style][0]*Mwidth+Box[Style][7])
                print(Box[Style][1]+options[count].center(Mwidth)+Box[Style][1])
                print(Box[Style][4]+Box[Style][0]*Mwidth+Box[Style][5])
                count+=1
            count +=1
        else:
            print("\n\n"+Box[1][0]*100+"\n\n")
            options.insert(0,r'options = ["'+options[0])
            options.reverse()
            options.insert(0,options[0]+r'"]')
            options.reverse()
            print(r"Style = "+str(Style))
            print(r"Box = [['\U00002550','\U00002551','\U00002554','\U00002557','\U0000255A','\U0000255D','\U00002560','\U00002563','\U00002566','\U00002569','\U0000256C'],['\U00002500','\U00002502','\U0000250C','\U00002510','\U00002514','\U00002518','\U0000251C','\U00002524','\U0000252C','\U00002534','\U0000253C']]")
            print(r"#Box[Style]: horiz, vert, TL corner, TR corner, BL corner, BR corner, Right Pointing T, LP T, DP T, UP T, cross")
            print(*options, sep = r'", "')
            for i in options:
                
                if Mwidth < len(i):
                    Mwidth = len(i)+1
                    
            if count ==0:
                print(r"Mwidth=" + str(Mwidth))
                print(r"print(Box[Style][2]+Box[Style][0]*Mwidth+Box[Style][3])")
                print(r"print(Box[Style][1]+options["+str(count)+r"].center(Mwidth)+Box[Style][1])")
                count+=1
            while count < len(options)-1:
                print(r"print(Box[Style][6]+Box[Style][0]*Mwidth)+Box[Style][7])")
                print(r"print(Box[Style][1]+options["+str(count)+r"].center(Mwidth)+Box[Style][1])")
                count+=1
            while count < len(options):
                print(r"print(Box[Style][6]+Box[Style][0]*Mwidth)+Box[Style][7])")
                print(r"print(Box[Style][1]+options["+str(count)+r"].center(Mwidth)+Box[Style][1])")
                print(r"print(Box[Style][4]+Box[Style][0]*Mwidth)+Box[Style][5])")
                count+=1            
            options.clear()
            print("\n\n"+Box[1][0]*100+"\n\n")
            print("Done!\nIf you'd like to go again, type 'menuMaker()'")
            break
        
menuMaker()
