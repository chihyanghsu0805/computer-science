// Copyright [year] <Copyright Owner>
#ifndef CPP_PROJECTS_BOOKSHOP_MANAGEMENT_MENU_H_
#define CPP_PROJECTS_BOOKSHOP_MANAGEMENT_MENU_H_

#include <iostream>

// #include "book.h"
// #include "supplier.h"
// #include "puchase.h"
// #include "emplyoee.h"
// #include "member.h"
// #include "sale.h"

namespace menu {
void book();
/*

void supplier_menu();
void purchase_menu();
void employee_menu();
void member_menu();
void sale_menu();
*/

void book() {
  // book::Book b;
  // Book* b = new Book();

  std::cout << " Books" << std::endl;
  std::cout << " 1. add" << std::endl;
  std::cout << " 2. UPDATE PRICE" << std::endl;
  std::cout << " 3. SEARCH" << std::endl;
  std::cout << " 4. UPDATE INVENTORY" << std::endl;
  std::cout << " 5. DISPLAY ALL" << std::endl;
  std::cout << " 6. RETURN TO MAIN MENU" << std::endl;
  std::cout << "Enter Choice: ";

  int c;
  std::cin >> c;

  switch (c) {
    /*

    case 1:
        b.add();
        break;
    case 2:
        b.update_price();
        break;
    case 3:
        b.search();
        break;
    case 4:
        b.update_inventory();
        break;
    case 5:
        b.display();
        break;
    case 6:
        return;
    default:
        std::cout << "Wrong Input" << std::endl;
        break;

    */
  }
  return;
}

void management() {
  std::cout << " BOOKSHOP MANGEMENT SYSTEM" << std::endl;
  std::cout << " 1. Books" << std::endl;
  std::cout << " 2. Suppliers" << std::endl;
  std::cout << " 3. Purchases" << std::endl;
  std::cout << " 4. Employees" << std::endl;
  std::cout << " 5. Members" << std::endl;
  std::cout << " 6. Sales" << std::endl;
  std::cout << " 7. Exit" << std::endl << std::endl << std::endl;
  std::cout << "Enter Choice: ";

  int c;

  std::cin >> c;

  // https://www.freecodecamp.org/news/getline-in-cpp-cin-getline-function-example/
  // getline only for string
  // std::getline(std::cin, c);

  switch (c) {
    case 1:
      system("cls");
      book();
      getchar();
      break;

    /*
    case 2:
        system("cls");
        supplier_menu();
        getch();
        break;

    case 3:
        system("cls");
        pur_menu();
        getch();
        break;
    case 4:
        system("cls");
        emp_menu();
        getch();
        break;
    case 5:
        system("cls");
        mem_menu();
        getch();
        break;
    case 6:
        system("cls");
        sal_menu();
        getch();
        break;
    */
    case 7:
      exit(1);

    default:
      std::cout << "Wrong Input" << std::endl;

      // https://stackoverflow.com/questions/41407242/declaring-the-getch-function
      // https://cplusplus.com/reference/cstdio/getchar/
      // https://www.quora.com/Why-dont-we-use-include-stdio-h-in-C
      // std::getchar();  // stdio.h
      getch();
      break;
  }

  return;
}

}  // namespace menu

#endif  // CPP_PROJECTS_BOOKSHOP_MANAGEMENT_MENU_H_
