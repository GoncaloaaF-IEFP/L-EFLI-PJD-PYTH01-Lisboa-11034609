//
// Created by Gonçalo Feliciano on 07/02/2025.
//

#include "funcs.h"
#include "src/unity.h"

void setUp(){}
void tearDown(){}


void test_soma_ok() {
    TEST_ASSERT_EQUAL(5, soma(3,2));
}

void test_sub() {
    TEST_ASSERT_EQUAL(1, subtracao(3,2));
}

void test_soma_nok() {
    TEST_ASSERT_EQUAL(5, soma(3,6));
    TEST_ASSERT_EQUAL(1,1);
    TEST_ASSERT_TRUE(1);
    TEST_ASSERT_FALSE(0);
    TEST_ASSERT_LESS_THAN(2, 4);
    TEST_ASSERT_LESS_OR_EQUAL(1,1);
    TEST_ASSERT_GREATER_THAN(1,1);
    TEST_ASSERT_GREATER_OR_EQUAL(1,1);
    TEST_ASSERT_NOT_EQUAL(1,3);
}

void test_div() {
    TEST_ASSERT_EQUAL_MESSAGE(1,8,"Msg se o teste falhar");

}

int main() {
    UNITY_BEGIN();
    RUN_TEST(test_soma_ok);
    RUN_TEST(test_soma_nok);
    RUN_TEST(test_sub);
    RUN_TEST(test_div);
    return UNITY_END();
}