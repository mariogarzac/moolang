var float x, y;
var file arch1;
var file arch2;
var char key, encrypted, decrypted, string, string_hash, encrypted_hash;
var char encrypted_file;
var char hmd5, h256;

main(){
    
     # String encryption
     arch2 = open("key.txt")
     key = generate_key()
     write(key, arch2)
     string = "this string";
     encrypted = encrypt(string, key)
     print("encrypted string ",encrypted)
     print("\n")

     string_hash = hash_md5(string)
     encrypted_hash = hash_md5(encrypted)

     if (string_hash -eq encrypted_hash){
            print("They are different. Is one encrypted?")
         }else{
            print("They are still the same!")
         }
     print("\n")

     decrypted = decrypt(string, key)
     print("decrypted string ", decrypted)
     print("\n")

     # File encryption
     arch1 = open("file1.txt")
     encrypted_file = encrypt(arch1, key)
     print("\n")

     # Hash check
     hmd5 = hash_md5(arch1)
     h256 = hash_sha256(arch1)
     print("hash_md5 ",hmd5)
     print("\n")
     print("hash_sha256 ", h256)
     print("\n")

     close(arch1)

}

    

#    print(key)
#    write("hello", arch1)
#    hash_sha256(arch1)
#    hash_md5(arch1)
