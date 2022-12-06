#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

int main() 
{
    std::fstream myFile;
    std::vector<int> allResults;
    int calCount = 0;

    myFile.open("input.txt", std::ios::in);
    if (myFile.is_open()) {
        std::string line;
        while (std::getline(myFile, line)) {
            if (line.empty()) {
                allResults.insert(allResults.end(), calCount);
                calCount = 0;
            }
            else {
                int num = stoi(line);
                calCount += num;
            }
        }
        myFile.close();
    }
    
    sort(allResults.begin(), allResults.end());
    std::cout << allResults.back() << std::endl;

    const int elvesNumber = 3;
    int result = 0;

    for (auto i = 0; i < elvesNumber; i++) {
        result += allResults.back();
        allResults.pop_back();
    }
    
    std::cout << result << std::endl;

}