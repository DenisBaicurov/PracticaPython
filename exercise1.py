
# from re import T
class Answay:
 def GetAns():
  while True:
    input_data = input("Введите число: ")
    if not input_data.isnumeric():
        print("Вы ввели не число. Попробуйте снова: ")
    elif not 1 < int(input_data) <8:
        print("Ваше число не диапазоне. Попробуйте снова")
    else:
        break
  return input_data

 def GetDay(nomber_day):
  DayWeek = [6,7]
  
  print(nomber_day)
  if nomber_day in (str)(DayWeek):
         print('совпало') 

  else :  
    print('не является')    

 GetDay(GetAns())          



  
