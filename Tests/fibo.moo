
func fiboIter(int n) -> int {
    var int prev, aux, res;
    var int i;

    prev = 0;
    res = 1;
    for (i = 1, i -lt n, i = i + 1){
            aux = prev;
            prev = res;
            res = aux + prev;
        }
    return res;
    }

func fiboRec(int n) -> int{
        var int res, x,y;
    
    if (n -lt 1) {
        res = n;
    } else {
        x = fiboRec(n - 1);
        y = fiboRec(n - 2);
        res = x + y;
    }
    return res;
}

main(){
    var int num, res;

    print("Enter a number: ")
    num = input()

    res = fiboIter(num);
    print("Iterative fibo is: ", res, "\n")

    res = fiboRec(num);
    print("Recursive fibo is: ", res, "\n")

    }
