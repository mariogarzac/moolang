

func iterFact(int n) -> int {
    var int res, i;
    res = 1;
    i = 1;
    
   for (i = 1, i -le n , i = i + 1){
       res = i * res;
       print(res, "\n")
   }

   return res;
}

func recFact(int n) -> int {
    var int res, x;
    if (n -eq 0)
      {
        res = 1;
       }
    else{
        x = recFact(n - 1);
        res = n * x;
        }
        return res;
}

 
main() {
    var int num, a, b, n;
    n = 0;

    print("Enter the number to calculate: ")
    num = input()
    a = iterFact(num);
    print("Iterative: ", a, "\n")

    b = recFact(num);
    print("Recursive : ", b, "\n")
}



