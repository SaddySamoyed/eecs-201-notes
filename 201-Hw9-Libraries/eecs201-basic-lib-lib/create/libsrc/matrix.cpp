#include <ostream>

#include <matrix.hpp>

Matrix::Matrix(int rows, int cols)
{
    this->m = rows;
    this->n = cols;

    this->buffer = new double[this->size()];
}

Matrix::~Matrix()
{
    delete[] this->buffer;
}

double &Matrix::operator()(int row, int col)
{
    return this->buffer[row * this->n + col];
}

const double &Matrix::operator()(int row, int col) const
{
    return this->buffer[row * this->n + col];
}

Matrix Matrix::multiply(const Matrix &other) const
{
    // eh no checks
    // A \dot B = C
    // A: this
    // B: other
    const Matrix &a = *this;
    const Matrix &b = other;
    Matrix c(a.rows(), b.cols());

    for (int i = 0; i < c.rows(); ++i) {
        for (int j = 0; j < c.cols(); ++j) {
            c(i,j) = 0;
            for (int k = 0; k < b.rows(); ++k) {
                c(i,j) += a(i,k) * b(k,j);
            }
        }
    }

    return c;
}

std::ostream &operator<<(std::ostream &os, const Matrix &matrix)
{
    for (int i = 0; i < matrix.rows(); ++i) {
        for (int j = 0; j < matrix.cols() - 1; ++j) {
            os << matrix(i,j) << ", ";
        }
        os << matrix(i,matrix.cols()-1);
        if (i < matrix.rows() - 1) os << std::endl;
    }
    return os;
}
