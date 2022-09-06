


class Verity:

    def input_boolean():
        print("X", "Y", "Z", "Rezult" )
        print("*"*15)
        for X in range(2):
            for Y in range(2):
                for Z in range(2):
                    rezult=not(X or Y or Z)== ((not X)and (not Y) and (not Z))
                    print(f"{X} {Y} {Z} - {rezult}")
    input_boolean()                


          
  

    # examination_verity()
