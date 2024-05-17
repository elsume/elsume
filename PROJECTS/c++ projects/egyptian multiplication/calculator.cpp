//MAIN FILE

#include "calculation.cpp"
#include <algorithm>
#include <iostream>
#include <limits>
#include <vector>
using namespace std;

int main() {
  int numA;
  int numB;
  char choice;

  do {
    while (true) {
      cout << "Enter the first number: ";
      if (cin >> numA) {
        break;
      } else {
        cerr << "Invalid input. Please enter an integer." << endl;
        // Clear the input buffer to handle incorrect input
        cin.clear();
        // Ignore any remaining characters in the buffer until a newline
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
      }
    }
    while (true) {
      cout << "Enter the second number: ";
      if (cin >> numB) {
        break;
      } else {
        cerr << "Invalid input. Please enter an integer." << endl;
        // Clear the input buffer to handle incorrect input
        cin.clear();

        // Ignore any remaining characters in the buffer until a newline
        cin.ignore(numeric_limits<std::streamsize>::max(), '\n');
      }
    }

    cout << endl;

    // checks for user input being zero multiplication
    if (checkZero(numA, numB) == true) {
      zeroMultiplication(numA, numB);
    }

    else if (checkZero(numA, numB) == false) {
      vector<int> secondList = firstCalculation(
          numB); // divides 2nd user input by 2 until its value is 1
      vector<int> firstList = secondCalculation(
          numA, secondList); // multiplies 1st user input by 2 until num of
                             // elements equals list2
      vector<int> thirdList = sumProduct(
          firstList,
          secondList); // makes list of nums thatll be added to find product
      printNum(firstList, secondList, thirdList);
      cout << endl;
      printSum(thirdList, numA, numB);
    }

    cout << "The product of " << numA << " and " << numB << " is "
         << numA * numB << '.' << endl;
    cout << endl;
    cout << "Do you want to run the program again? (y for yes): ";
    cin >> choice;

  } while (choice == 'y');
  return 0;
}