
var int x;
var int i;


func funcDos(int cont ,int b) -> int {
    print("x vale ", cont, b)
    for (x = cont, x -lt 10, x = x+1){
            print(x, " ")

        }
        print("\n")
    return x;
    }

main(){
    
    i = funcDos(1, 2);
    print(i)

}

