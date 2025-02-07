cmake_minimum_required(VERSION 3.30)
project(Demo_testes C)

set(CMAKE_C_STANDARD 11)

add_executable(Demo_testes main.c
        funcs.c
        funcs.h
        tests.c)
