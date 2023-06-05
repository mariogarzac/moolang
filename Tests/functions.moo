
var int i;
var int n;
var int x[19];

func printNums(int n) -> int {
    if (n -lt 15)
       {
        print(n, "\n")
        return printNums(n + 1);
       }
    else{
        return n;
        }
    }


main(){
    
    i = printNums(10);
    print(i)

}

