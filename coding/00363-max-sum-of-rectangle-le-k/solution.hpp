#include <iostream>
#include <set>
#include <vector>

using std::vector;
using std::set;
using std::cout;
using std::endl;

class Solution {
public:
  int maxSumSubmatrix(vector<vector<int> >& matrix, int k) {
    vector<vector<int> > S = matrix;  // copy it
    int m = S.size();
    if (m == 0)
        return 0;
    int n = S[0].size();
    if (n == 0)
        return 0;

    // compute prefix S
    for (int i = 0; i < m; i++)
      for (int j = 1; j < n; j++)
        S[i][j] += S[i][j-1];
    for (int i = 1; i < m; i++)
      for (int j = 0; j < n; j++)
        S[i][j] += S[i-1][j];

    int max = -999999999;
    for (int j = 0; j < n; j++) {
      for (int q = j; q < n; q++) {
        set<int> bst;
        vector<int> T(m, 0);
        for (int p = 0; p < m; p++) {
          int anchor = j == 0 ? 0 : S[p][j-1];
          T[p] = S[p][q] - anchor;
        }
        for (int i = m-1; i >= 0; i--) {
          bst.insert(-T[i]);
          int anchor = i == 0 ? 0 : T[i-1];
          auto it_lower = bst.lower_bound(-k-anchor);
          if (it_lower != bst.end()) {
            int sum = -*it_lower - anchor;
            max = sum > max ? sum : max;
          }
        }
        if (max == k)
          return max;
      }
    }
    return max;
  }
};
