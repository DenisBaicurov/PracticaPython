from traceback import TracebackException


class Determination_of_the_plane_number:
    def Input_Number():
        while type:
            input_number = input("Введите число: ")
            try:
                input_number=float(input_number)
            except ValueError:
                print('Неверный ввод числа!')
                continue
            except TypeError :
                print('Неверный ввод числа!') 
                continue
            if(input_number==0) :
                print('Число не должно равняться 0')  
            else :
                break        
           
        return float(input_number)

    def Of_the_plane_number(x, y):
        print (x)
        print (y)
        if(int(x)>0 and int(y)>0):
            print("1 четверть")
        elif(int(x)<0 and int(y)>0):
            print("2 четверть")
        elif(int(x)>0 and int(y)<0):
            print("3 четверть")
        elif(int(x)<0 and int(y)<0):
            print("4 четверть") 
   #     else:print(0)  
    Of_the_plane_number(Input_Number(),Input_Number())       