
var int res, x;

#func iterFact(int n) -> int {
    #var int res, i;
    #res = 1;
    #i = 1;
    #
   #for (i = 1, i -le n , i = i + 1){
       #res = i * res;
       #print(res, "\n")
   #}
#
   #return res;
#}

func recFact(int n) -> int {
    print("n is ",n, "\n")
    if (n -eq 0)
      {
        res = 1;
       }
    else{
        x = recFact(n - 1);
        print("x is ",x, "\n")
        res = n * x;
        }
    return res;
}

 
main() {
    var int num, a, b, n;
    #n = 0;

    #print("Enter the number to calculate: ")
    #num = input()
    num = 10;
    #a = iterFact(num);
    #print("Iterative: ", a, "\n")

    b = recFact(num);
    print("Recursive : ", b, "\n")
}



