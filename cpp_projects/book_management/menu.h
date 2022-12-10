#include <iostream>

#include "book.h"
#include "supplier.h"
//#include "puchase.h"
//#include "emplyoee.h"
//#include "member.h"
//#include "sale.h"

namespace menu {

    void book_menu();
    void supplier_menu();
    /*
    void purchase_menu();
    void employee_menu();
    void member_menu();
    void sale_menu();

    void sale_menu() {
        int c;
        Sale s;
        std::cout << "*************************************************" << std::endl;
        std::cout << "                 SALES MENU" << std::endl;
        std::cout << "*************************************************" << std::endl;
        std::cout << "   1. Add New Bill" << std::endl;
        std::cout << "   2. Total Sales Of The Year" << std::endl;
        std::cout << "   3. RETURN TO MAIN MENU" << std::endl << std::endl << std::endl;
        std::cout << "Enter Your Choice : ";
        std::cin >> c;
        switch (c) {
            case 1:
                s.add();
                break;
            case 2:
                s.find_total_sales();
                break;
            case 3:
                return;
            default:
                std::cout << "Wrong Input" << std::endl << "Invalid Input";
                break;
        }
    }

    void member_menu() {
        int c;
        Member m;
        m.refresh();
        std::cout << "*************************************************" << std::endl;
        std::cout << "                 MEMBERS MENU" << std::endl;
        std::cout << "*************************************************" << std::endl;
        std::cout << "   1. New Member" << std::endl;
        std::cout << "   2. Search Member" << std::endl;
        std::cout << "   3. RETURN TO MAIN MENU" << std::endl << std::endl << std::endl;
        std::cout << "Enter Your Choice : ";
        std::cin >> c;
        switch (c) {
            case 1:
                m.add_mem();
                break;
            case 2:
                m.search_mem();
                break;
            case 3:
                return;
            default:
                std::cout << "Wrong Input" << std::endl << "Invalid Input";
                break;
        }
    }

    void employee_menu() {
        int c;
        Employee e;
        std::cout << "*************************************************" << std::endl;
        std::cout << "                 EMPLOYEE MENU" << std::endl;
        std::cout << "*************************************************" << std::endl;
        std::cout << "   1. New Employee" << std::endl;
        std::cout << "   2. Search Employee" << std::endl;
        std::cout << "   3. Assign Manager" << std::endl;
        std::cout << "   4. View All" << std::endl;
        std::cout << "   5. Update Salary" << std::endl;
        std::cout << "   6. RETURN TO MAIN MENU" << std::endl << std::endl << std::endl;
        std::cout << "Enter Your Choice : ";
        std::cin >> c;
        switch (c) {
            case 1:
                e.add_emp();
                break;
            case 2:
                e.search_emp();
                break;
            case 3:
                e.assign_mgr_stat();
                break;
            case 4:
                e.display();
                break;
            case 5:
                e.update_sal();
                break;
            case 6:
                return;
            default:
                std::cout << "Wrong Input" << std::endl << "Invalid Input";
                break;
        }
    }

    void purchase_menu() {
        int c;
        Purchase p;
        std::cout << "*************************************************" << std::endl;
        std::cout << "                PURCHASES MENU" << std::endl;
        std::cout << "*************************************************" << std::endl;
        std::cout << "   1. New Order" << std::endl;
        std::cout << "   2. View All" << std::endl;
        std::cout << "   3. Cancel Order" << std::endl;
        std::cout << "   4. Received Order" << std::endl;
        std::cout << "   5. RETURN TO MAIN MENU" << std::endl << std::endl << std::endl;
        std::cout << "Enter Your Choice : ";
        std::cin >> c;
        switch (c) {
            case 1:
                p.new_ord();
                break;
            case 2:
                p.view();
                break;
            case 3:
                p.mar_cancel();
                break;
            case 4:
                p.mark_reciv();
                break;
            case 5:
                return;
            default:
                std::cout << "Wrong Input" << std::endl << "Invalid Input";
                break;
        }
    }
    */
    void supplier_menu() {
        
        int c;
        supplier::Supplier s;
        std::cout << "*************************************************" << std::endl;
        std::cout << "                SUPPLIER MENU" << std::endl;
        std::cout << "*************************************************" << std::endl;
        std::cout << "   1. ADD" << std::endl;
        std::cout << "   2. REMOVE" << std::endl;
        std::cout << "   3. SEARCH" << std::endl;
        std::cout << "   4. RETURN TO MAIN MENU" << std::endl << std::endl << std::endl;
        std::cout << "Enter Your Choice: ";
        std::cin >> c;
        
        switch (c) {
            case 1:
                s.add();
                break;
            case 2:
                s.remove();
                break;
            case 3:
                s.search();
                break;
            case 4:
                return;
            default:
                std::cout << "Wrong Input" << std::endl;
                break;
        }
    }
    
    void book_menu() {
        
        book::Book b;

        int c;
        std::cout << "*************************************************" << std::endl;
        std::cout << "                  BOOK MENU" << std::endl;
        std::cout << "*************************************************" << std::endl;
        std::cout << "   1. ADD" << std::endl;
        std::cout << "   2. UPDATE PRICE" << std::endl;
        std::cout << "   3. SEARCH" << std::endl;
        std::cout << "   4. UPDATE INVENTORY" << std::endl;
        std::cout << "   5. DISPLAY ALL" << std::endl;
        std::cout << "   6. RETURN TO MAIN MENU" << std::endl << std::endl << std::endl;
        std::cout << "Enter Your Choice: ";
        std::cin >> c;

        switch (c) {
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
        }
        
        return;
    }
     
    void main_menu() {
        
        int c;
        std::cout << "*************************************************" << std::endl;
        std::cout << "         BOOKSHOP MANGEMENT SYSTEM" << std::endl;
        std::cout << "*************************************************" << std::endl;
        std::cout << "   1. BOOKS" << std::endl;
        std::cout << "   2. SUPPLIERS" << std::endl;
        std::cout << "   3. PURCHASES" << std::endl;
        std::cout << "   4. EMPLOYEES" << std::endl;
        std::cout << "   5. MEMBERS" << std::endl;
        std::cout << "   6. SALES" << std::endl;
        std::cout << "   7. EXIT" << std::endl << std::endl << std::endl;
        std::cout << "Enter Your Choice: ";
        
        std::cin >> c;
        
        switch (c) {

            case 1:
                system("cls");
                book_menu();
                getch();
                break;
            
            case 2:
                system("cls");
                supplier_menu();
                getch();
                break;
            /*
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
                getch();                
                break;
        }
        
        return;
    }

}