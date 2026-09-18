cmake_minimum_required(VERSION 3.16)
project(autodiff_test_package CXX)

find_package(autodiff REQUIRED CONFIG)

add_executable(example example.cpp)
target_link_libraries(example PRIVATE autodiff::autodiff)
target_compile_features(example PRIVATE cxx_std_17)
