


class Verity:

    def input_boolean():
        while True:
            input_data = input ("Введите число:0 или 1 ")
            if not input_data.isnumeric():
                print("Вы ввели не число. Попробуйте снова: ")
            elif not 0 <= int(input_data) <= 1:
                print("Ваше число не диапазоне. Попробуйте снова")
            else:
                break
            
        
      #  print(bool(int(input_data)))
        return (bool(int(input_data)))

    x=input_boolean()
    y=input_boolean()
    z=input_boolean()

    print(not(x|y|z))
    print((not x)&(not y)&(not z))
    print((not((x|y|z)))==(not x)&(not y)&(not z))

          
  

    # examination_verity()
