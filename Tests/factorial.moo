func recursiveFact(int n) -> int {
    var int res, x;


    if (n -eq 0) {
        res = 1;
    } else {
        x =  recursiveFact(n - 1)
        res = (n * x);
    }

    return res;
}

func iterFact(int n) -> int {
    var int res, i;
    var int m, y, a,b;
    res = 1;
    
    for (i = 1, i -lt (n + 1), i = i + 1){

        }

    return res;
}

main() {
    var int num, a;

    print("Enter the number to calculate: ")
    num = input()

    a = recursiveFact(num)

    print("Recursive: ", a)

    a = iterFact(num)

    print("Iterative: ", a)
}
