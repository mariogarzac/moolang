
func iterFact(int n) -> int {
    var int res, i;
    res = 1;
    i = 1;
    
   for (i = 1, i -le n , i = i + 1){
       res = i * res;
   }

    return res;
}

func recFact(int n) -> int {
    if (n -lt 5)
       {
        print(n)
        return recFact(n + 1);
       }
    else{
        return n;
        }
    }

main() {
    var int num, a, n;
#    n = 0;
#    a = recFact(n);
#    print(a)

    print("Enter the number to calculate: ")
    num = input()
    a = iterFact(num);
    print("Iterative: ", a)
}
