//UNIT TESTS

#include "calculation.cpp"
#include <cassert>
#define NDBUG
#include <iostream>
using namespace std;

int main() {
  // INITIALIZATION OF VECTORS INCLUDED IN THE TESTS
  vector<int> testAList1{10, 5, 2, 1};
  vector<int> testAList2{17352, 8676, 4338, 2169, 1084, 542, 271, 135,
                         67,    33,   16,   8,    4,    2,   1};
  vector<int> testAList3{35, 17, 8, 4, 2, 1};

  vector<int> fiveVals{1, 2, 3, 4, 5};
  vector<int> sixVals{1, 2, 3, 4, 5, 6};
  vector<int> threeVals{1, 2, 3};

  vector<int> testBList1{10, 20, 40, 80, 160};
  vector<int> testBList2{1234, 2468, 4936};
  vector<int> testBList3{14, 28, 56, 112, 224, 448};

  vector<int> test3listA{12, 24, 48, 96};
  vector<int> test3listB{9, 4, 2, 1};
  vector<int> test3listC{12, 96};

  vector<int> test4listA{5, 10, 20, 40, 80, 160, 320};
  vector<int> test4listB{97, 48, 24, 12, 6, 3, 1};
  vector<int> test4listC{5, 160, 320};

  cout << "Testing started" << endl;

  assert(checkZero(0, 1) == true);
  assert(checkZero(1, 0) == true);
  assert(checkZero(14, 35) == false);

  assert(((firstCalculation(10)) == testAList1) == true);
  assert(((firstCalculation(17352)) == testAList2) == true);
  assert(((firstCalculation(35)) == testAList3) == true);

  assert((secondCalculation(10, fiveVals) == testBList1) == true);
  assert((secondCalculation(1234, threeVals) == testBList2) == true);
  assert((secondCalculation(14, sixVals) == testBList3) == true);

  assert((sumProduct(test3listA, test3listB) == test3listC) == true);
  assert((sumProduct(test4listA, test4listB) == test4listC) == true);

  cout << "Testing completed" << endl;

  return 0;
}
