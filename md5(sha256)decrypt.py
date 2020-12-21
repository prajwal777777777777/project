from hashlib import md5,sha256;
import pyinputplus;
#todo:please provide the small wordlist file absolute path.

#do not use too large wordlist.
try:

    path=pyinputplus.inputFilepath(prompt="Enter the absolute path of wordlist:")
    given_sha_256=pyinputplus.inputStr(prompt="Enter the sha256 hash:")
    password_list=[]
    #opening the file 
    print("Running...")
    with open(path,"rb") as f:
        file_content_list=f.readlines()
        
        for i in file_content_list:
            i=i.strip()
            password_list.append(i)

#todo:closing the file as we get content of the given_wordlist in password_list which is list.
#todo:converting password to md5.
    md5_list=[]

    for password in password_list:
        md5_password=md5((password)).hexdigest();
        md5_list.append(md5_password);

    #todo:now u need to encrypt these wordlist password to sha256 and check if the given_list password match the ur sha256 encoded password.
    sha_256_list=[]
    #todo:converting the md5 encrypted password to sha256.
    for passwords in md5_list:
        sha_256_password=sha256(passwords.encode()).hexdigest();
        sha_256_list.append(sha_256_password);

    #todo:after converting checking the encrypted hash in our sha256_list or not.
    if(given_sha_256 in sha_256_list):
        index=sha_256_list.index(given_sha_256);
        print("PASSWORD FOUND.".center(100,"-"));
        print(f"Password={password_list[index].decode()}");
    #todo:if the password match then it will return the plain text password from the given wordlist.
    else:
        print("password not found in the given wordlist.");
    #todo:if password doesnot match then it will give this output.


except KeyboardInterrupt:
    print("\nbye.");

except:
    print("An unknown error has occured.")
    
    #you can use name __name__==__main__ or #!/usr/bin/python3
