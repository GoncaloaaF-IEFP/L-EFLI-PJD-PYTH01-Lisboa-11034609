cmake_minimum_required(VERSION 3.30)
project(demoFuncs2 C)

set(CMAKE_C_STANDARD 11)

add_executable(demoFuncs2 main.c
        op_math.c
        op_math.h
        saudacoes.c
        saudacoes.h
)
