var int a[10];


func find() -> void{
    var int i, num;
    a[0] = 2;
    a[1] = 11;
    a[2] = 4;
    a[3] = 5;
    a[4] = 4;
    a[5] = 7;
    a[6] = 5;
    a[7] = 1;
    a[8] = 3;
    a[9] = 11;
    num = input()
    for (i = 0, i -lt 10, i = i + 1){
        if (a[i] -eq num){
                print("Found it in position", i ,"\n")
            }
        }

    }


main(){
    var int i;
    find()
        
    }


