
#running program repeatedly
def play(n):
    n+=1
    while True:
        # Import libraries
        import matplotlib.pyplot as plt
        import numpy as np
        from shapely.geometry import  LineString
        import winsound
        import math

        soundfile="D:\\College Work\\Projects\\Graphia\\graphia.wav"

        #function for calculating ncr
        def NcR(n,r):
            e=math.factorial(n)
            k=math.factorial(r)
            m=math.factorial(n-r)
            p=e/(k*m)
            return(p)
        #function for calculating gcd
        def gcd(m,n):
            cf=[]
            for i in range(1,min(m,n)+1):
                if (m%i)==0 and (n%i)==0:
                    cf.append(i)
            return(cf[-1])     

        #main program
        
        soundfile10="D:\\College Work\\Projects\\Graphia\\Graphia_intro.wav"
        winsound.PlaySound(soundfile10, winsound.SND_FILENAME|winsound.SND_ASYNC)
        print("Welcome to Graphia")
        print("Graphia is a program that can plot graphs of various functions and find their intersections with other functions as well")
        print("It can plot graphs with the x axis having limit of (-10,10) and y axis having limit (-10,10)")
        print("Graphia can do the following jobs:")
        print("Please choose your response")
        print("1.Plot any polynomial function")
        print("2.Plot trigonometric functions")
        print("3.Solve any two trigonometric functions simultaneously and find their solution")
        print("4.Solve any trigonometric function with a polynomial function")
        print("5.Plot any polygon and find it's area")
        print("6.Find the factorial of a given number")
        print("7.Sorting of numbers in ascending order")
        print("8.Check for a number whether it is prime or not")
        print("9.Input the any two terms of an AP and find the nth term and sum upto the nth term of the AP")
        print("10.Input the any two terms of an GP and find the nth term and sum upto the nth term of the GP")
        print("11.Calculate sum of first n natural numbers")
        print("12.Calculate sum of squares of the first n natural numbers")
        print("13.Calculate sum of cubes of the first n natural numbers")
        print("14.Calculate the number of ways to select n1 things out of n2 things")
        print("15.Calculate GCD of two numbers:")
        print("16.solve any two polynomial functions simultaneously and find their solutions")
        print("Enter 17 to exit")
        response=int(input("Enter your response: "))
        if response==1:
            print("enter the equation (but onlt polynomial function in the form y=ax^4+bx^3+cx^2+dx+e and always write all values upyo e):")
            a1=float(input("enter a "))
            b1=float(input("enter b "))
            c1=float(input("enter c "))
            d1=float(input("enter d "))
            e1=float(input("enter e "))
            # Creating vectors X and Y
            x = np.linspace(-10, 10, 100)
            y = a1*x**4+b1*x**3+c1*x**2+d1*x+e1
            fig = plt.figure(figsize = (14, 8))
            # Create the plot
            plt.plot(x, y, 'r-.', label ='Polynomial function')
            plt.title('GRAPHIA')
            plt.xlabel('x-axis')
            plt.ylabel('y-axis')
            #second plot to find zeros
            y2=0*x
            plt.plot(x,y2,'g:', label ='X axis')
            # Add features to our figure
            plt.legend()
            plt.grid(True, linestyle =':')
            plt.xlim([-10, 10])
            plt.ylim([-10, 10])
            #getting intersection
            line_1 = LineString(np.column_stack((x, y)))
            line_2 = LineString(np.column_stack((x, y2)))
            intersection=line_1.intersection(line_2)
            if intersection.geom_type == 'MultiPoint':
                            plt.plot(*LineString(intersection).xy, 'o')
            elif intersection.geom_type == 'Point':
                            plt.plot(*intersection.xy, 'ro')
            #showing intersection
            print("The first list of coordinates are x coordinates and the second are the respective y coordinates")
            if intersection.geom_type == 'MultiPoint': 
                x, y = LineString(intersection).xy
                print("intersection:",x, y)
            elif intersection.geom_type == 'Point':
                x, y = intersection.xy
                print("intersection:",x, y)
            else:
                print("no intersection")
            #showing plot
            winsound.PlaySound(soundfile, winsound.SND_FILENAME|winsound.SND_ASYNC)
            plt.show()    
        elif response==2:
            print("enter the equation (but onlt trigonometric function in the form y=sin(1*x) and always input coefficient of x ):")
            trig=input("Enter the equation:")
            func=trig[2:5]
            if func=="sin":
                    x = np.linspace(-10, 10, 100)
                    fig = plt.figure(figsize = (14, 8))
                    t=int(trig[6:(trig.find("*"))])
                    y=np.sin(t*x)
                    plt.plot(x,y, 'r-.', label ='sin(t*x)')

            elif trig[2:6]=="cos(":
                    x = np.linspace(-10, 10, 100)
                    fig = plt.figure(figsize = (14, 8))
                    t=int(trig[6:(trig.find("*"))])
                    y=np.cos(t*x)
                    plt.plot(x,y, 'r-.', label ='cos(t*x)')
            elif func=="tan":
                    x = np.linspace(-10, 10, 100)
                    fig = plt.figure(figsize = (14, 8))
                    t=int(trig[6:(trig.find("*"))])
                    y=np.tan(t*x)
                    plt.plot(x,y, 'r-.', label ='tan(t*x)')
            elif trig[2:7]=="cosec":
                    x = np.linspace(-10, 10, 100)
                    fig = plt.figure(figsize = (14, 8))
                    k=int(trig[8:(trig.find("*"))])
                    y=np.sin(k*x)**-1
                    plt.plot(x,y, 'r-.', label ='cosec(k*x)')
            elif func=="sec":
                    x = np.linspace(-10, 10, 100)
                    fig = plt.figure(figsize = (14, 8))
                    t=int(trig[6:(trig.find("*"))])
                    y=np.cos(t*x)**-1
                    plt.plot(x,y, 'r-.', label ='sec(t*x)')
            else:
                x = np.linspace(-10, 10, 100)
                fig = plt.figure(figsize = (14, 8))
                t=int(trig[6:(trig.find("*"))])
                y=np.tan(t*x)**-1
                plt.plot(x,y, 'r-.', label ='cot(t*x)')
            plt.title('GRAPHIA')
            plt.xlabel('x-axis')
            plt.ylabel('y-axis')
            # Add features to our figure
            plt.legend()
            plt.grid(True, linestyle =':')
            plt.xlim([-10, 10])
            plt.ylim([-10, 10])
            winsound.PlaySound(soundfile, winsound.SND_FILENAME|winsound.SND_ASYNC)
            plt.show()
        elif response==3:
            #first equation
            print("enter the first equation (but onlt trigonometric function in the form y=sin(1*x) and always input coefficient of x ):")
            trig=input("Enter the equation:")
            func=trig[2:5]
            x = np.linspace(-10, 10, 100)
            fig = plt.figure(figsize = (14, 8))
            if func=="sin":
                    t=int(trig[6:(trig.find("*"))])
                    y=np.sin(t*x)
                    plt.plot(x,y, 'g:', label ='First trigonometric function')
            elif trig[2:6]=="cos(":
                    t=int(trig[6:(trig.find("*"))])
                    y=np.cos(t*x)
                    plt.plot(x,y, 'g:', label ='First trigonometric function')
            elif func=="tan":
                    t=int(trig[6:(trig.find("*"))])
                    y=np.tan(t*x)
                    plt.plot(x,y, 'g:', label ='First trigonometric function')
            elif trig[2:7]=="cosec":
                    k=int(trig[8:(trig.find("*"))])
                    y=np.sin(k*x)**-1
                    plt.plot(x,y, 'g:', label ='First trigonometric function')
            elif func=="sec":
                    t=int(trig[6:(trig.find("*"))])
                    y=np.cos(t*x)**-1
                    plt.plot(x,y, 'g:', label ='First trigonometric function')
            else:
                t=int(trig[6:(trig.find("*"))])
                y=np.tan(t*x)**-1
                plt.plot(x,y, 'g:', label ='First trigonometric function')
            #second equation
            print("enter the second equation (but onlt trigonometric function in the form y=sin(1*x) and always input coefficient of x ):")
            trig=input("Enter the equation:")
            func=trig[2:5]
            if func=="sin":
                    t=int(trig[6:(trig.find("*"))])
                    y2=np.sin(t*x)
                    plt.plot(x,y2, 'r-.', label ='Second trigonometric function') 
            elif trig[2:6]=="cos(":
                    t=int(trig[6:(trig.find("*"))])
                    y2=np.cos(t*x)
                    plt.plot(x,y2, 'r-.', label ='Second trigonometric function') 
            elif func=="tan":
                    t=int(trig[6:(trig.find("*"))])
                    y2=np.tan(t*x)
                    plt.plot(x,y2, 'r-.', label ='Second trigonometric function') 
            elif trig[2:7]=="cosec":
                    k=int(trig[8:(trig.find("*"))])
                    y2=np.sin(k*x)**-1
                    plt.plot(x,y2, 'r-.', label ='Second trigonometric function') 
            elif func=="sec":
                    t=int(trig[6:(trig.find("*"))])
                    y2=np.cos(t*x)**-1
                    plt.plot(x,y2, 'r-.', label ='Second trigonometric function') 
            else:
                t=int(trig[6:(trig.find("*"))])
                y2=np.tan(t*x)**-1
                plt.plot(x,y2, 'r-.', label ='Second trigonometric function') 
            plt.title('GRAPHIA')
            plt.xlabel('x-axis')
            plt.ylabel('y-axis')
            # Add features to our figure
            plt.legend()
            plt.grid(True, linestyle =':')
            plt.xlim([-10, 10])
            plt.ylim([-10, 10])
            #getting intersection
            line_1 = LineString(np.column_stack((x, y)))
            line_2 = LineString(np.column_stack((x, y2)))
            intersection=line_1.intersection(line_2)
            if intersection.geom_type == 'MultiPoint':
                            plt.plot(*LineString(intersection).xy, 'o')
            elif intersection.geom_type == 'Point':
                            plt.plot(*intersection.xy, 'ro')
            #showing intersection
            print("The first list of coordinates are x coordinates and the second are the respective y coordinates")                
            if intersection.geom_type == 'MultiPoint': 
                x, y = LineString(intersection).xy
                print("intersection:",x, y)
            elif intersection.geom_type == 'Point':
                x, y = intersection.xy
                print("intersection:",x, y)
            else:
                print("no intersection")
            #showing plot
            winsound.PlaySound(soundfile, winsound.SND_FILENAME|winsound.SND_ASYNC)
            plt.show()    
        elif response==4:
            #first polynomial function
            print("enter the equation (but onlt polynomial function in the form y=ax^4+bx^3+cx^2+dx+e and always write all values upyo e):")
            a1=float(input("enter a "))
            b1=float(input("enter b "))
            c1=float(input("enter c "))
            d1=float(input("enter d "))
            e1=float(input("enter e "))
            # Creating vectors X and Y
            x = np.linspace(-10, 10, 100)
            y = a1*x**4+b1*x**3+c1*x**2+d1*x+e1
            fig = plt.figure(figsize = (14, 8))
            #second trigonometric function
            print("enter the second equation (but onlt trigonometric function in the form y=sin(1*x) and always input coefficient of x ):")
            trig=input("Enter the equation:")
            func=trig[2:5]
            if func=="sin":
                    t=int(trig[6:(trig.find("*"))])
                    y2=np.sin(t*x)
            elif trig[2:6]=="cos(":
                    t=int(trig[6:(trig.find("*"))])
                    y2=np.cos(t*x)
            elif func=="tan":
                    t=int(trig[6:(trig.find("*"))])
                    y2=np.tan(t*x)
            elif trig[2:7]=="cosec":
                    k=int(trig[8:(trig.find("*"))])
                    y2=np.sin(k*x)**-1
            elif func=="sec":
                    t=int(trig[6:(trig.find("*"))])
                    y2=np.cos(t*x)**-1
            else:
                t=int(trig[6:(trig.find("*"))])
                y2=np.tan(t*x)**-1
            plt.plot(x, y2, 'r-.', label ='Trigonometric function')    
            plt.plot(x, y, 'g:', label ='Polynomial function')
            plt.title('GRAPHIA')
            plt.xlabel('x-axis')
            plt.ylabel('y-axis')
            # Add features to our figure
            plt.legend()
            plt.grid(True, linestyle =':')
            plt.xlim([-10, 10])
            plt.ylim([-10, 10])
            #getting intersection
            line_1 = LineString(np.column_stack((x, y)))
            line_2 = LineString(np.column_stack((x, y2)))
            intersection=line_1.intersection(line_2)
            if intersection.geom_type == 'MultiPoint':
                            plt.plot(*LineString(intersection).xy, 'o')
            elif intersection.geom_type == 'Point':
                            plt.plot(*intersection.xy, 'ro')
            #showing intersection
            print("The first list of coordinates are x coordinates and the second are the respective y coordinates")                
            if intersection.geom_type == 'MultiPoint': 
                x, y = LineString(intersection).xy
                print("intersection:",x, y)
            elif intersection.geom_type == 'Point':
                x, y = intersection.xy
                print("intersection:",x, y)
            else:
                print("no intersection")                
            #showing plot
            winsound.PlaySound(soundfile, winsound.SND_FILENAME|winsound.SND_ASYNC)    
            plt.show()    
        elif response==5:
            coor=int(input("Enter the number of vertices of polygon:"))
            x2=[]
            y2=[]
            if coor<3:
                print("invalid input")
            else:
                for i in range(0,coor):
                    x=float(input("Enter the x coordinate:"))
                    y=float(input("Enter the respective y coordinate:"))
                    x2.append(x)
                    y2.append(y)
                x3=x2[0]
                y3=y2[0]
                x2.append(x3)
                y2.append(y3)
                plt.plot(x2,y2)
                winsound.PlaySound(soundfile, winsound.SND_FILENAME|winsound.SND_ASYNC)    
                T=0
                i=0
                while i<(coor-1):
                    T+=x2[i]*y2[i+1]-y2[i]*x2[i+1]
                    i+=1
                T+=x2[coor-1]*y2[0]-y2[coor-1]*x2[0]
                area=T/2
                if area<0:
                    area=area*(-1)
                    print("Area of polygon",area)
                else:
                    print("Area of polygon",area)
                plt.show()
        elif response == 6:
            factorial=int(input("Enter the number whose factorial is to be calculated:"))
            num=1
            if factorial<2:
                          print("Factorial:",num)
            else:
                ter=1
                i=factorial
                while i >=1:
                    ter*=i
                    i-=1
                print("Factorial:",ter)
        elif response == 7:
            listt=[]
            terms=int(input("Enter the numbers of terms to be sorted"))
            for i in range(0,terms):
                r=float(input("Enter the term"))
                listt.append(r)
            listt.sort()
            print("Sorted terms in ascending order:",listt)
        elif response == 8:
            jer=int(input("Enter the number to be checked:"))
            check=[]
            p=[]
            for i in range(2,jer):
                if jer%i==0:
                    check.append(i)
                else:
                    p.append(i)
            if len(check)==0:
                print("The number is prime")
            else:
                print("The number is not prime")
        elif response == 9:
            tfirst=int(input("Specify the term number:"))
            a1=float(input("Enter the term of the AP"))
            tsecond=int(input("Specify the term number:"))
            a2=float(input("Enter the term of the AP"))
            n=int(input("Enter the number of term which you wish to findout and calculate the sum upto it"))
            if tfirst>tsecond:
                fw=a1-a2
                gta=tfirst-1
                gtf=tsecond-1
                gtk=gta-gtf
                d=fw/gtk #calculating common difference
                first_term=a1-(tfirst-1)*d
                tn=first_term+(n-1)*d
                uu=n/2
                uk=2*first_term+(n-1)*d
                sn=uu*uk
            else:
                fw=a2-a1
                gta=tfirst-1
                gtf=tsecond-1
                gtk=gtf-gta
                d=fw/gtk #calculating common difference
                first_term=a1-(tfirst-1)*d
                tn=first_term+(n-1)*d
                uu=n/2
                uk=2*first_term+(n-1)*d
                sn=uu*uk
            print(n,"th term is:",tn)
            print("sum upto",n,"th term is",sn)     
        elif response == 10:
            tfirst=int(input("Specify the term number:"))
            a1=float(input("Enter the term of the GP"))
            tsecond=int(input("Specify the term number:"))
            a2=float(input("Enter the term of the GP"))
            n=int(input("Enter the number of term which you wish to findout and calculate the sum upto it"))
            if tfirst>tsecond:
                tree=a1/a2
                r_n=tfirst-1
                r_b=tsecond-1
                ktg=r_n-r_b
                r=tree**(1/ktg)
                t1=a1/(r**r_n)
                tn=t1*(r**(n-1))
                hg=r**n
                gf=hg-1
                sn=t1*gf/(r-1)
            else:
                tree=a2/a1
                r_n=tfirst-1
                r_b=tsecond-1
                ktg=r_b-r_n
                r=tree**(1/ktg)
                t1=a1/(r**r_n)
                tn=t1*(r**(n-1))
                hg=r**n
                gf=hg-1
                sn=t1*gf/(r-1)
            print(n,"th term is:",tn)
            print("sum upto",n,"th term is",sn)
        elif response == 11:
            n=int(input("Enter n:"))
            we=n*(n+1)
            sn=we/2
            print("sum upto",n,"th term is",sn)
        elif response == 12:
            n=int(input("Enter n:"))
            wq=n*(n+1)*(2*n+1)
            sn=wq/6
            print("sum upto",n,"th term is",sn)
        elif response == 13:
            n=int(input("Enter n:"))
            wr=n**2
            wt=(n+1)**2
            wd=wr*wt
            sn=wd/4
            print("sum upto",n,"th term is",sn)
        elif response == 14:
            n1=int(input("Enter n1:"))
            n2=int(input("Enter n2:"))
            result=NcR(n2,n1)
            print("Number of ways:",result)
        elif response == 15:
            m=int(input("Enter the first number:"))
            n=int(input("Enter the second number:"))
            result=gcd(m,n)
            print("GCD of the numbers is",result)
        elif response == 17:
            print("successful exit")
            break
        else:
            print("enter the first equation (but onlt polynomial function in the form y=ax^4+bx^3+cx^2+dx+e and always write all values upyo e):")
            #first plot
            a3=float(input("enter a "))
            b3=float(input("enter b "))
            c3=float(input("enter c "))
            d3=float(input("enter d "))
            e3=float(input("enter e "))
            # Creating vectors X and Y
            x = np.linspace(-10, 10, 100)
            fig = plt.figure(figsize = (14, 8))
            y = a3*x**4+b3*x**3+c3*x**2+d3*x+e3
            #second plot
            print("enter the second equation (but onlt polynomial function in the form y=ax^4+bx^3+cx^2+dx+e and always write all values upyo e):")
            a2=float(input("enter a "))
            b2=float(input("enter b "))
            c2=float(input("enter c "))
            d2=float(input("enter d "))
            e2=float(input("enter e "))
            #create plot
            y2 = a2*x**4+b2*x**3+c2*x**2+d2*x+e2
            plt.plot(x, y, 'r-.', label ='First polynomial function')
            plt.plot(x, y2, 'g:', label ='Second polynomial function')
            plt.title('GRAPHIA')
            plt.xlabel('x-axis')
            plt.ylabel('y-axis')
            # Add features to our figure
            plt.legend()
            plt.grid(True, linestyle =':')
            plt.xlim([-10, 10])
            plt.ylim([-10, 10])
            #getting intersection
            line_1 = LineString(np.column_stack((x, y)))
            line_2 = LineString(np.column_stack((x, y2)))
            intersection=line_1.intersection(line_2)
            if intersection.geom_type == 'MultiPoint':
                            plt.plot(*LineString(intersection).xy, 'o')
            elif intersection.geom_type == 'Point':
                            plt.plot(*intersection.xy, 'ro')
            #showing intersection
            print("The first list of coordinates are x coordinates and the second are the respective y coordinates")                
            if intersection.geom_type == 'MultiPoint': 
                x, y = LineString(intersection).xy
                print("intersection:",x, y)
            elif intersection.geom_type == 'Point':
                x, y = intersection.xy
                print("intersection:",x, y)
            else:
                print("no intersection")
            #showing the plot
            winsound.PlaySound(soundfile, winsound.SND_FILENAME|winsound.SND_ASYNC)    
            plt.show()    


kill=int(input("Enter 5 to start "))
if kill == 5:
    play(kill)
else:
    print("Invalid input")