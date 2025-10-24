cmake_minimum_required(VERSION 4.0)
project(Matryoshka_Project C CXX)

set(CMAKE_C_STANDARD 11)


add_executable(Matryoshka_Project
        backup.c
        main.c
        playground.c
        sendIP.c
        cmake-build-debug/test.c
        replace.cpp
        helper.c
        helper.h)
