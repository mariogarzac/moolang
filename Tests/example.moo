 var int x,y;
 var file arch1, arch2, arch3;
 var char arr[5];

 func test() -> int 
{
  var int z;
  var file hashed_file;
  var char key;
  z = 0;
   
  if (z -gt 10){
      key = generate_key()
      arch1 = open("file.txt")
      hashed_file = read(arch1)
      hash_md5(hashed_file)
      hash_sha256(hashed_file)
      encrypt(hashed_file, key)
      decrypt(hashed_file, key)
      return 2;
      } else{
              return 3;
          }

  return 1;
}

func aSimpleFunc() -> void {
        while((count + 1) -lt 10){
            count = count + 1;
                print("Still less than 10")
            }
    }

main(){

    if (x -gt 1){
            
        }

 # this is a comment

  for x = 1 in range (0,1,x = 1){
      print("Hello")
  }

   arr = hash_md5(arch1)

}
