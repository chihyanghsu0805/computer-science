// Copyright [year] <Copyright Owner>
#ifndef CPP_PROJECTS_BOOK_MANAGEMENT_CONSTANTS_H_
#define CPP_PROJECTS_BOOK_MANAGEMENT_CONSTANTS_H_

// For a static/global string constant
// use a C style string instead: "static const char host[]".

namespace connection_constants {
static const char host[] = "localhost";
static const char user[] = "root";
static const char password[] = "0000";
static const char database[] = "bookshop_management";
static const int port = 3306;
};  // namespace connection_constants
// extern const int PASSWORD;

#endif  // CPP_PROJECTS_BOOK_MANAGEMENT_CONSTANTS_H_
