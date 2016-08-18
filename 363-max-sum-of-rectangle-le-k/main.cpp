#include <cassert>
#include <vector>
#include <cstdlib>
#include <iostream>
#include "solution.hpp"

using std::vector;
using std::cout;
using std::endl;

void test_0() {
  Solution sol;
  vector<vector<int> > matrix1(0);
  assert(sol.maxSumSubmatrix(matrix1, 10) == 0);
  vector<vector<int> > matrix2(0);
  vector<int> row(0);
  matrix2.push_back(row);
  assert(sol.maxSumSubmatrix(matrix2, 10) == 0);
}

void test_1() {
  Solution sol;
  vector<vector<int> > matrix = {
    {1, 0, 1}, {0, -2, 3}};
  assert(sol.maxSumSubmatrix(matrix, 2) == 2);
}

// copy the matrix
int ref(vector<vector<int> > matrix, int k) {
  int m = matrix.size();
  int n = matrix[0].size();
  for (int i = 0; i < m; i++)
    for (int j = 1; j < n; j++)
      matrix[i][j] += matrix[i][j-1];
  for (int i = 1; i < m; i++)
    for (int j = 0; j < n; j++)
      matrix[i][j] += matrix[i-1][j];
  int max = -999999999;
  for (int p = 0; p < m; p++) {
    for (int q = 0; q < n; q++) {
      for (int i = p; i < m; i++) {
        for (int j = q; j < n; j++) {
          int anchor_pq = p == 0 || q == 0 ? 0 : matrix[p-1][q-1];
          int anchor_p = p == 0 ? 0 : matrix[p-1][j];
          int anchor_q = q == 0 ? 0 : matrix[i][q-1];
          int sum = matrix[i][j] - anchor_p - anchor_q + anchor_pq;
          if (sum <= k && sum > max)
            max = sum;
        }
      }
    }
  }
  return max;
}

void test_2() {
  Solution sol;
  int m = 50, n = 40;
  vector<vector<int> > matrix;
  for (int i = 0; i < m; i++) {
    vector<int> row(n);
    for (int j = 0; j < n; j++) {
      row[j] = std::rand() % 200 - 100;
    }
    matrix.push_back(row);
  }
  for (int i = 0; i < 10; i++) {
    int k = std::rand() % 200 - 100;
    sol.maxSumSubmatrix(matrix, k);
    assert(sol.maxSumSubmatrix(matrix, k) == ref(matrix, k));
  }
}

void test_3() {
  Solution sol;
  int m = 1, n = 3;
  int k = 0;
  vector<vector<int> > matrix = {{2, 2, -1}};
  assert(ref(matrix, k) == -1);
  assert(sol.maxSumSubmatrix(matrix, k) == -1);
}

void test_4() {
  Solution sol;
  int m = 3, n = 4;
  int k = 3;
  vector<vector<int> > matrix = {
    {5, -4, -3, 4}, {-3, -4, 4, 5}, {5, 1, 5, -4}};
  assert(ref(matrix, k) == 2);
  assert(sol.maxSumSubmatrix(matrix, k) == 2);
}

int main(int argc, char** argv) {
  test_0();
  test_1();
  test_2();
  test_3();
  test_4();
  return 0;
}
