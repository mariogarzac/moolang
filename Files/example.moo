
var int x,y,res1,res2;
var file arch;
var char[32] key;

func nombre() -> void {
    print("ESTE ES EL ARCHIVO DE MARIO GARZA CHAPA");
}

func greet() -> void {
    print("Hola! Esta es la suma: ");

}


func sum(int a, int b) -> int {
    return a + b;
}

main(){
    arch = read(arch)

    x = 10;
    y = 11;

    print(greet, sum(x,y))
    print(greet, sum(z,w))
    res1 = sum(x,y)
    res2 = sum(z,w)

    if (res1 -gt res2){
            print("la primera es mayor")
    }else{
            print("la segunda es mayor")
     }
    
     key = generate_key()
     encrypt(arch, key)
     close(arch)

}
