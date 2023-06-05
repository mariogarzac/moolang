var int mat1[3][3];
var int mat2[3][3];
var int res[3][3];

func multiply() -> void {
   var int i, j, k, aux;
mat1[0][0] = 1;
mat1[0][1] = 1;
mat1[0][2] = 1;
mat1[1][0] = 1;
mat1[1][1] = 1;
mat1[1][2] = 1;
mat1[2][0] = 1;
mat1[2][1] = 1;
mat1[2][2] = 1;

mat2[0][0] = 1;
mat2[0][1] = 1;
mat2[0][2] = 1;
mat2[1][0] = 1;
mat2[1][1] = 1;
mat2[1][2] = 1;
mat2[2][0] = 1;
mat2[2][1] = 1;
mat2[2][2] = 1;


mat2[0][0] = 0;
mat2[0][1] = 0;
mat2[0][2] = 0;
mat2[1][0] = 0;
mat2[1][1] = 0;
mat2[1][2] = 0;
mat2[2][0] = 0;
mat2[2][1] = 0;
mat2[2][2] = 0;

    while (i -lt 3){
        while (j -lt 3){
            while (k -lt 3){
                aux = res[i][j];
                res[i][j] = aux + mat1[i][k] * mat2[k][j];
                k = k + 1;
                }
            j = j + 1;
                }

        i = i + 1;
        }
}
  
main(){
    multiply()

    }
