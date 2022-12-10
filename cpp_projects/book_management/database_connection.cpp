// Copyright [year] <Copyright Owner>
#include "cpp_projects/book_management/database_connection.h"

#include <mysql.h>

#include <iostream>

database::Connection::Connection(const std::string host, const std::string user,
                                 const std::string password,
                                 const std::string database, const int port) {
  db_conn = mysql_init(NULL);
  if (!db_conn)
    std::cout << "MySQL initialization failed." << std::endl;
  else
    std::cout << "MySQL initialized." << std::endl;

  db_conn =
      mysql_real_connect(db_conn, host.c_str(), user.c_str(), password.c_str(),
                         database.c_str(), port, NULL, 0);

  if (!db_conn)
    std::cout << "Connection Error." << std::endl;
  else
    std::cout << "Connected." << std::endl;
}

database::Connection::~Connection() { mysql_close(db_conn); }
