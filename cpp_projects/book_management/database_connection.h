// Copyright [year] <Copyright Owner>"  [legal/copyright]
#ifndef CPP_PROJECTS_BOOK_MANAGEMENT_DATABASE_CONNECTION_H_
#define CPP_PROJECTS_BOOK_MANAGEMENT_DATABASE_CONNECTION_H_

#include <mysql.h>

#include <string>

namespace database {

class Connection {
  MYSQL* db_conn;

 public:
  Connection(const std::string,  // host
             const std::string,  // user
             const std::string,  // password
             const std::string,  // database
             const int);         // port

  ~Connection();
};

}  // namespace database
#endif  // CPP_PROJECTS_BOOK_MANAGEMENT_DATABASE_CONNECTION_H_
