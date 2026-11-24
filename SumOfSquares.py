first_number = 1
second_number = 0
third_number = 0
while (  first_number < 10) :
    while (  second_number < 10) : 
        while (  third_number < 10):
            square = ( first_number * first_number ) + ( second_number * second_number )
            + ( third_number * third_number )
            number = ( first_number * 100) + ( second_number * 10 ) + ( third_number );
            if ( square == number ) :
                print(number)
            third_number+= 1
        second_number+= 1
    first_number+= 1
