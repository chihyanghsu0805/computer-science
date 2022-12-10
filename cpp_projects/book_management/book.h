#include <iostream>
#include <sstream>
#include <mysql.h>

extern MYSQL_RES * res_set;
extern MYSQL * conn;
extern MYSQL_ROW row;

extern std::stringstream statement;
extern std::string query;
extern const char * q;

namespace book {
    
    class Book {
        int id; // Primary Key
        std::string name;
        std::string author;
        int price;
        int quantity;
        std::string table = "book";

    public:	
        void add();
        void update_price();
        void search();
        void update_inventory();
        void display();                
    };

    void Book::add() {
        
        std::cout << "Enter the BOOK NAME: " ;
        std::cin >> name;
        
        std::cout << "Enter the BOOK AUTHOR: ";
        std::cin >> author;
        
        std::cout << "Enter the BOOK PRICE: ";
        std::cin >> price;
        
        std::cout << "Enter the BOOK QUANTITY: ";
        std::cin >> quantity;

        statement.str("");
        statement << "INSERT INTO " << table << "(NAME, AUTHOR, PRICE, QUANTITY) VALUES('" << name << "','" << author << "'," << price << "," << quantity << ");";
        query = statement.str();
        q = query.c_str();        
        mysql_query(conn, q);
        res_set = mysql_store_result(conn);

        if (!(res_set))
            std::cout << "BOOK added." << std::endl;
        else
            std::cout << "Entry error." << std::endl;
    }
    
    void Book::update_price() {
        
        char choice;
        
        std::cout << "Enter the BOOK ID for PRICE update: ";
        std::cin >> id;

        statement.str("");
        statement << "SELECT NAME,PRICE FROM " << table << " WHERE id = " << id << ";";
        query = statement.str();
        q = query.c_str();
        mysql_query(conn,q);
        res_set = mysql_store_result(conn);

        if((row = mysql_fetch_row(res_set)) != NULL) {

            std::cout << "The BOOK NAME is: " << row[0] << std::endl;
            std::cout << "The BOOK PRICE is: " << row[1] << std::endl;
            std::cout << "Do you want to update the BOOK PRICE? [Y/N]: ";
            std::cin >> choice;
            
            if (choice == 121 || choice == 89) {
                
                std::cout << "Enter the new BOOK PRICE: ";
                std::cin >> price;
                
                statement.str("");
                statement << "UPDATE " << table << " SET PRICE = " << price << " WHERE id = " << id << ";";
                query = statement.str();
                q = query.c_str();
                mysql_query(conn, q);
                res_set = mysql_store_result(conn);
                
                if (!(res_set))
                    std::cout << "BOOK PRICE updated." << std::endl;
                else
                    std::cout << "Entry Error." << std::endl;
            } else {
                std::cout << "BOOK PRICE not cupdated.";
            }
        } else {
            std::cout << "BOOK not found.";
        }
        
    }

    void Book::search() {
        
        std::cout << "Enter BOOK ID to search: ";
        std::cin >> id;
        
        statement.str("");
        statement << "SELECT * FROM " << table << " WHERE id = " << id << ";";
        query = statement.str();
        q = query.c_str();
        mysql_query(conn,q);
        res_set = mysql_store_result(conn);
        
        if((row = mysql_fetch_row(res_set)) != NULL) {
            std::cout << "BOOK ID:" << row[0] << std::endl;
            std::cout << "BOOK NAME: " << row[1] << std::endl;
            std::cout << "BOOK AUTHOR: " << row[2] << std::endl;
            std::cout << "BOOK PRICE: " << row[3] << std::endl;
            std::cout << "BOOK QUANTITY: " << row[4] << std::endl;
            std::cout << std::endl;
        } else {
            std::cout << "BOOK not found." << std::endl;
        }
    }

    void Book::update_inventory() {
        // NEED PURCHASE
        
        int b_id[100], qty[100], i = 0, max;
        
        statement.str("");
        statement << "Select book_id,qty from purchases where receives = 'T' and inv IS NULL;";        
        query = statement.str();
        q = query.c_str();
        mysql_query(conn,q);
        res_set = mysql_store_result(conn);

        statement.str("");        
        statement << "Update purchases set inv = 1 where receives = 'T' and inv IS NULL;";
        query = statement.str();
        q = query.c_str();
        mysql_query(conn,q);

        while((row = mysql_fetch_row(res_set)) != NULL) {
            b_id[i] = atoi(row[0]);
            qty[i] = atoi(row[1]);
            i++;
        }
        
        max = i;
        for(i = 0; i <= max; i++) {
            
            statement.str("");
            statement << "update books set qty = " << qty[i] << " where id = " << b_id[i] << ";";
            query = statement.str();
            q = query.c_str();
            mysql_query(conn,q);
            
        }
        std::cout << "The orders received have been updated.";
    }

    void Book::display() {
        
        int i = 0;
        
        statement.str("");
        statement << "SELECT * FROM " << table << ";";
        query = statement.str();
        q = query.c_str();
        mysql_query(conn,q);
        res_set = mysql_store_result(conn);
        
        while((row = mysql_fetch_row(res_set)) != NULL) {

            std::cout << "BOOK ID: " << ++i << std::endl;
            std::cout << "BOOK NAME: " << row[1] << std::endl;
            std::cout << "BOOK AUTHOR: " << row[2] << std::endl;
            std::cout << "BOOK PRICE: " << row[3] << std::endl;
            std::cout << "BOOK QUANTITY: " << row[4] << std::endl;
            std::cout << std::endl;

        }
    }
}