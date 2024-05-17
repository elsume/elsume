//CONTAINS ALL THE FUNCTIONS USED IN THE PROGRAM

#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <vector>
using namespace std;

// checks if any user input contains zero
bool checkZero(int numA, int numB) { return (numA == 0 || numB == 0); }
// prints out a default table for multiplication with zero
void zeroMultiplication(int numA, int numB) {
  cout << setw(10) << right << 'A' << "   " << setw(5) << left << 'B' << "   "
       << "Comment" << endl;
  cout << "--------------------------------------------------------------------"
          "--------------------------"
       << endl;
  cout << setw(10) << right << numA << " | " << setw(5) << left << numB << " | "
       << "A number is equal to zero, so the calculation will end." << endl;
}
// divides second user input by zero until it reaches 1; makes vector with all
// the values
vector<int> firstCalculation(int num) {
  vector<int> numList;
  int B;
  B = abs(num);
  while (B > 0) {
    numList.push_back(B);
    B = B / 2;
  }
  return numList;
}
// multiplies first user input by two until the amount of values equals the
// amount of elements in the list passed into the function
vector<int> secondCalculation(int num, vector<int> list) {
  vector<int> numList;
  int A;
  A = abs(num);
  for (int i = 0; i < list.size(); i++) {
    numList.push_back(A);
    A = A * 2;
  }
  return numList;
}
// makes a list of A values that are connected to odd B values
vector<int> sumProduct(vector<int> listA, vector<int> listB) {
  vector<int> numList;
  for (int i = 0; i < listB.size(); i++) {
    if (listB.at(i) % 2 != 0) {
      numList.push_back(listA.at(i));
    }
  }
  return numList;
}
// prints table of all values
void printNum(vector<int> listA, vector<int> listB, vector<int> listC) {
  cout << setw(10) << right << 'A' << "   " << setw(5) << left << 'B' << "   "
       << "Comment" << endl;
  cout << "--------------------------------------------------------------------"
          "--------------------------"
       << endl;
  for (int i = 0; i < listB.size(); i++) {
    if (listB.at(i) % 2 != 0) {
      cout << setw(10) << right << listA.at(i) << " | " << setw(5) << left
           << listB.at(i) << " | "
           << "Number is odd, so it will be a part of the final sum." << endl;
      cout << "----------------------------------------------------------------"
              "------------------------------"
           << endl;
    } else {
      cout << setw(10) << right << listA.at(i) << " | " << setw(5) << left
           << listB.at(i) << " | "
           << "" << endl;
      cout << "----------------------------------------------------------------"
              "------------------------------"
           << endl;
    }
  }
}
// adds all A values connected to odd B values, with the sum being the product
void printSum(vector<int> listC, int numA, int numB) {
  int sum;
  cout << "Add all A values that have an odd B value to find the product:"
       << endl;
  for (int i = 0; i < listC.size(); i++) {
    if (i == static_cast<int>((listC.size()) - 1)) {
      cout << listC.at(i) << endl;
      sum = sum + listC.at(i);
    } else {
      cout << listC.at(i) << " + ";
      sum = sum + listC.at(i);
    }
  }
  if ((numA < 0 && numB > 0) || (numA > 0 && numB < 0) == true) {
    cout << "= -" << sum << endl;
  } else {
    cout << "= " << sum << endl;
  }
}
