#include <stdio.h>#include <stdlib.h>int main(){
   int num;
   FILE *fptr;

   // use appropriate location if you are using MacOS or Linux
   fptr = fopen("C:\\program.txt","w");
   ////////////////////////aaaaaaaaaaaaaaaaaaaaaaaaaaa
   //

   printf("Enter num: ");
   scanf("%d",&num);

   fprintf(fptr,"%d",num);
   fclose(fptr);

   return 0;
}