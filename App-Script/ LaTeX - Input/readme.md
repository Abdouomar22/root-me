The script provided creaate a pfd file from a Latex file (with tex extention) .
Our flag is on /challenge/app-script/ch23/.passwd
So the idea is to create a latex file contain an input command to include the content of .passwd file

![Screenshot from 2024-08-12 23-24-58](https://github.com/user-attachments/assets/50efa6d4-cd4b-498c-82ef-1904d8f2789c)

we got the generated pdf then we use scp to get the pdf file into out local host

$ scp -P 2222 app-script-ch23@challenge02.root-me.org:/tmp/(enter ur random value here)/main.pdf ./main.pdf
open the pdf file .

![Screenshot from 2024-08-12 23-32-15](https://github.com/user-attachments/assets/95790b74-9be9-4aa1-b74f-27446f38115e)

So now we need a way to make latex file escape special char for comments which is % .
After search i find i package that input a file as plaintext without trait special characters or commands .
The package is verbatim .

![Screenshot from 2024-08-12 23-36-00](https://github.com/user-attachments/assets/3016dfa6-033b-4f82-a7b9-dc09977d1f19)

Finaly upload the file again using scp then u get the flag .

![Untitled design](https://github.com/user-attachments/assets/961b7d5f-eee2-4ab0-af1b-68e0d109ffa4)
