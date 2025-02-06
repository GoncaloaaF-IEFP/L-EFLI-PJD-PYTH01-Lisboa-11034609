//
//  main.cpp
//  demo_c++
//
//  Created by Gonçalo Feliciano on 31/10/2024.
//

#include <iostream>

int main(int argc, const char * argv[]) {
    // tipo nome
   
   int idade;
   int ano = 2024;
   
   /*
    \n  - new line - muda de linha
    
    */
  
    std::cout << "Ola Mundo\n";
    
   idade = 30;
    std::cout << "Ola Mundo\n" << idade << "/n";
   
   int anoNasc = ano - idade;
   
   
   printf("se nasceu em %i tem %i\n",anoNasc, idade);
   
   
   if (idade > 18){
       
       printf("Adulto\n");
       
   }else{
       
       printf("não Adulto\n");
       
   }
   printf("---------if--------\n");
   
   idade = 23;
   int foo = 10;
   
   if (idade > 21 && !(foo == 10)){
       
       printf("Adulto e pode beber\n");
     
   }else if (idade > 18){
      
       printf("Adulto\n");
     
   }else{
       printf("não Adulto\n");
       
   }
   printf("---------while--------\n");
   // while
   
   while (foo > 0) {
       printf("%i\n", foo);
       foo -= 1;
   }
   
   
   //do-while
   printf("-------do-while----------\n");
   
   int myVar = 68;
   do {
       
       printf("%i\n", myVar);
       myVar -= 30;
       
   } while (myVar > 20);
   
   printf("--------for---------\n");
   // for
   
   //for(cond init; cond paragem; inc){}
   for(int i = 0; i < 100 ; i += 5 ){
       
       printf("%i\n", i);

   }
   
   printf("--------input---------\n");
   // scanf
   
   int myData;
   
    std::cout << "Qual a sua idade: ";
    std::cin >> myData;
   
    std::cout << "a sua idede é " << myData << "\n";
   
    return 0;
}
