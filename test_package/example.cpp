#include <cstdlib>
#include <iostream>

#include <autodiff/forward/dual.hpp>
using namespace autodiff;

dual f(dual x, dual y)
{
    return x * x + y * y;
}

int main()
{
    dual x = 2.0;
    dual y = 3.0;

    const double dfdx = derivative(f, wrt(x), at(x, y));

    std::cout << "f(x, y) = " << f(x, y) << "\n";
    std::cout << "df/dx = " << dfdx << "\n";

    if (dfdx != 2.0 * val(x))
    {
        std::cerr << "autodiff conan package sanity check failed\n";
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}
