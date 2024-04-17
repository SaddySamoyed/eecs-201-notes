#ifndef __MATRIX_HPP__
#define __MATRIX_HPP__

/**
 * 2-D matrix class
 */
class Matrix
{
public:
    Matrix(int rows, int cols);
    ~Matrix();
    double &operator()(int row, int col);
    const double &operator()(int row, int col) const;

    Matrix multiply(const Matrix &other) const;

    int size() const {return this->m * this->n;}
    int rows() const {return this->m;}
    int cols() const {return this->n;}
private:
    int m; // rows
    int n; // cols

    double *buffer; // row-major linearized buffer
};

std::ostream &operator<<(std::ostream &os, const Matrix &matrix);

#endif//__MATRIX_HPP__
