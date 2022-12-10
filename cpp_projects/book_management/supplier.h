#include <iostream>
#include <sstream>
#include <mysql.h>

extern MYSQL_RES * res_set;
extern MYSQL * conn;
extern MYSQL_ROW row;

extern std::stringstream statement;
extern std::string query;
extern const char * q;

namespace supplier {

    class Supplier{
        int id;	//Primary Key
        std::string name;
        long int phone;
        std::string address;        
    public:
        void add();
        void remove();
        void search();
    };
    
    void Supplier::add() {
        
        std::cout << "Enter the Supplier Name : ";
        std::cin >> name;
        
        std::cout << "Enter Phone no. : ";
        std::cin >> phone;
        
        std::cout << "Enter the address: ";
        std::cin >> address;
        
        statement.str("");
        statement << "Insert into suppliers(name,phone_no,addr) values('" << name << "'," << phone << ",'" << address << "');";
        query = statement.str();
        q = query.c_str();
        
        mysql_query(conn,q);
        res_set = mysql_store_result(conn);
        
        if (!(res_set))
            std::cout << "Supplier Record Inserted Successfully" << std::endl;
        else
            std::cout << "Entry ERROR !" << std::endl;
    }

    void Supplier::remove() {
        std::cout << "Enter the supplier id to remove the Supplier : ";
        std::cin >>  id;
        statement.str("");
        statement << "Delete from suppliers where id = " << id << ";";
        query = statement.str();
        q = query.c_str();
        mysql_query(conn,q);
        std::cout << "Supplier Removed.";
    }

    void Supplier::search() {
        std::cout << "Enter the supplier id to find the Supplier details : ";
        std::cin >>  id;
        statement.str("");
        statement << "Select * from suppliers where id = " << id << ";";
        query = statement.str();
        q = query.c_str();
        mysql_query(conn,q);
        res_set = mysql_store_result(conn);
        if((row = mysql_fetch_row(res_set)) != NULL) {
            std::cout << "Details of Supplier Id : " << row[0] << std::endl;
            std::cout << "Name : " << row[1] << std::endl;
            std::cout << "Phone no. : " << row[2] << std::endl;
            std::cout << "Address: " << row[3] << std::endl;            
        } else {
            std::cout << "No Supplier Found!!";
        }
    }
}