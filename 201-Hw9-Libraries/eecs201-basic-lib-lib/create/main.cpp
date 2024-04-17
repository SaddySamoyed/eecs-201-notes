#include <iostream>
#include <matrix.hpp>

int main(int argc, char *argv[])
{
    constexpr int dim1 = 5;
    constexpr int dim2 = 2;

    Matrix a(dim1,dim2);
    for (int i = 0; i < dim1; ++i) {
        for (int j = 0; j < dim2; ++j){
           a(i,j) = (double)((i + 1) * (j + 1));
        }
    }

    Matrix b(dim2,dim1);
    for (int i = 0; i < dim2; ++i) {
        for (int j = 0; j < dim1; ++j){
           b(i,j) = (double)((i + 1) * (j + 1));
        }
    }

    std::cout << a << std::endl;
    std::cout << 'x' << std::endl;
    std::cout << b << std::endl;
    std::cout << '=' << std::endl;
    std::cout << a.multiply(b) << std::endl;

    return 0;
}
