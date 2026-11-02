#include <gtest/gtest.h>

#include "mathops.hpp"

TEST(Arithmetic, BasicAddition) {
    EXPECT_EQ(mathops::add(2, 3), 5);
}

TEST(Arithmetic, AdditionWithNegative) {
    EXPECT_EQ(mathops::add(-4, 1), -3);
}

TEST(Arithmetic, AdditionWithZero) {
    EXPECT_EQ(mathops::add(0, 7), 7);
}
