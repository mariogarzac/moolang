
var int x;
var int i;
var int n;

#func funcDos(int cont ,int b) -> int {
#    for (x = cont, x -lt 10, x = x+1){
#            print(x, " ")
#
#        }
#    return x;
#    }

func tres(int n) -> int {
    if (n -lt 5)
       {
        print(n)
        return tres(n + 1);
       }
    else{
        return n;
        }
    }


main(){
    
    i = tres(n);
    print(i)

}

#0 main None None $13
#1 -lt 3000 6000 5750
#2 gotof 5750 None $10
#3 era None None tres
#4 + 3000 6001 3001
#5 param 3001 None 3000
#6 gosub None 3 $1
#7 return None None 3002
#8 = 3002 None 3
#9 goto None None $11
#10 return None 3000 3003
#11 = 3003 None 3
#12 endfunc None None None
#13 era None None tres
#14 param 6002 None 3000
#15 gosub None 3 $1
#16 = 3 None 1
#17 print None None 1
#18 endfunc None None None

