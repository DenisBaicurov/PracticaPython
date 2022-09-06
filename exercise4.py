def Get_Number_Quater():
    while type:
        input_number=input('Введите номер четвети от 1 до 4 :')
        try:
                input_number=int(input_number)
        except ValueError:
                print('Неверный ввод числа!')
                continue
        except TypeError :
                print('Неверный ввод числа!') 
                continue
        if  not 0<int (input_number)<5 :
                print('Ваше число не в диапозоне, попробуйте снова ввести') 
        else:
            break
    return int (input_number)  

def Get_Range(i): 
      
    if i==1 :
        print('1 четверть X>0 и Y>0')
    elif i==2:
        print('2 четверть X<0 и Y>0')
    elif i==3:
        print('3 четверть X<0 и Y<0')    
    elif  i==4:
        print('4 четверть X>0 и Y<0')     
    else :
        print ('что-то не так ввели') 

Get_Range(Get_Number_Quater())