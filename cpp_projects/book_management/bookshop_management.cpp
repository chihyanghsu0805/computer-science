// Copyright [year] <Copyright Owner>"  [legal/copyright]
// https://github.com/Aryan-Khanijo/Bookshop-Management-System-CPP-Project/blob/master/BookShopManagement.cpp
// g++ -o bookshop_management.exe
// bookshop_management.cpp
// database_connection.cpp
// constants.cpp
// -I "C:/Program Files/MySQL/MySQL Server 8.0/include/"
// -L "C:/Program Files/MySQL/MySQL Server 8.0/lib/"
// -l libmysql

// #include <iostream>
// #include <windows.h>
// #include <conio.h>

#include "./constants.h"
#include "./database_connection.h"

// #include "menu.h"

int main() {
  // Database should already exists.
  database::Connection* database_connection = new database::Connection(
      connection_constants::host, connection_constants::user,
      connection_constants::password, connection_constants::database,
      connection_constants::port);

  /*

  while (true) {
      system("cls");
      menu::main_menu();

      if (!std::cin) {
          std::cin.clear();
          std::cin.ignore();
      }
  }
  */

  return 0;
}
