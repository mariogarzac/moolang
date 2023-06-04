
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

main(){
    var int num, res;

    print("Enter number to calculate: ")
    num = input()

    res = fiboIter(num);
    print("Iterative fibo is: ", res, "\n")



    }
