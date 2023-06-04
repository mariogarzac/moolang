

func iterFact(int n,int b) -> int {
    var int res, i;
    res = 1;
    i = 1;
    
   for (i = 1, i -le n , i = i + 1){
       res = i * res;
       print(res, "\n")
   }

   return res;
}

#func recFact(int n) -> int {
#    var int res, x;
#    if (n -eq 0)
#       {
#        res = 1;
#       }
#    else{
#        x = recFact(n - 1) * n;
#        res = n * x;
#        }
#        return res;
#}

func recFact(int n) -> int {
 if (n -lt 10)
       {
        print(n, "\n")
        return recFact(n + 1);
       }
    else{
        return n;
        }
    }
 
main() {
    var int num, a, b, n;
    n = 0;

    print("Enter the number to calculate: ")
    num = input()
    a = iterFact(num, a);
    print("Iterative: ", a, "\n")

    b = recFact(num);
    print("Recursive : ", b, "\n")
}
#0 main None None $14
#1 -lt 3000 6000 5750
#2 gotof 5750 None $12
#3 print None None 3000
#4 print None None 8000
#5 era None None recFact
#6 + 3000 6001 3002
#7 param 3002 None 3000
#8 gosub None 0 $1
#9 = 0 None 3003
#10 return None None 0
#11 goto None None $13
#12 return 3000 None 0
#13 endfunc None None None
#14 = 6002 None 3002
#15 print None None 8001
#16 input None None 3003
#17 = 3003 None 3000
#18 era None None recFact
#19 param 3000 None 3000
#20 gosub None 0 $1
#21 = 0 None 3004
#22 = 0 None 3001
#23 print None None 8002
#24 print None None 3001
#25 print None None 8000
#26 endprog None None None

