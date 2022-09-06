import math
def Input_Coordinate():
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
          
            break        
           
    return float(input_number)

def Get_Distance(x,y,x1,y1):

  print('Выведим рассиояние между точками')
  print(math.sqrt(pow((y-x),2)+pow((y1-x1),2)))

Get_Distance(Input_Coordinate(),Input_Coordinate(),Input_Coordinate(),Input_Coordinate()) 

