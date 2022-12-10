// https://github.com/Aryan-Khanijo/Bookshop-Management-System-CPP-Project/blob/master/BookShopManagement.cpp
// g++ -o a.exe book_management.cpp  -I "C:/Program Files/MySQL/MySQL Server 8.0/include/" -L "C:/Program Files/MySQL/MySQL Server 8.0/lib/" -l libmysql

#include <iostream>
#include <mysql.h>

#include <windows.h>
#include <conio.h>

#include "menu.h"

// DATABASE AND TABLE SHOULD ALREADY EXIST
// CREATE DATABASE bookmanagement;
// use bookmanagement;
/*
CREATE TABLE IF NOT EXISTS book (
  id int NOT NULL AUTO_INCREMENT,
  name varchar(255),
  author varchar(255),
  price int,
  quantity int,
  PRIMARY KEY (id)
);
CREATE TABLE IF NOT EXISTS supplier (
  id int NOT NULL AUTO_INCREMENT,
  name varchar(255),
  author varchar(255),
  price int,
  quantity int,
  PRIMARY KEY (id)
);
*/

#define HOST "localhost"
#define USER "root"
#define PASS "0000"
#define DATABASE "bookmanagement"
#define PORT 3306
#define PASSWORD 0000

MYSQL_RES * res_set;
MYSQL * conn;
MYSQL_ROW row;

std::stringstream statement;
std::string query;
const char * q;
/*
void pass() {
    
    int num = 0;
    std::cout << "Enter Password: ";
    for (int i=0; i < 4; ++i) {

        num = num * 10 + (getch() - 48);
        std::cout << "*";

    }

    if (num == PASSWORD) {
        
        std::cout << std::endl << std::endl << "Correct Password" << std::endl << std::endl;
        std::cout << "Press any key ...";
        getch();

    } else {

        std::cout << std::endl << std::endl << "Incorrect Password" << std::endl << std::endl;
        std::cout << "Press any key...";
        getch();
        exit(1);

    }
    return ;
}
*/
int main() {

    //pass();

    conn = mysql_init(NULL);
    conn = mysql_real_connect(conn, HOST, USER, PASS, DATABASE, PORT, NULL, 0);

    if (conn) {

        while (conn) {
            
            system("cls");
            menu::main_menu();
            
            if (!std::cin) {
                std::cin.clear();
                std::cin.ignore();
            }
        
        }        

    } else {

        system("cls");
        std::cout << "Error while connection to database." << std::endl;
		getch();

	}
	return 0;
}
