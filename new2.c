#include <stdio.h>#include <stdlib.h>int main(){
   FILE *fptr;

   // use appropriate location if you are using MacOS or Linux

   if(fptr == NULL)
   {
      printf("Error!");   
      exit(1);             
   }

   printf("Enter num: ");
   scanf("%d",&num);

   fclose(fptr);

   return 0;
}