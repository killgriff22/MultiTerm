#include <chrono>
#include <thread>
#include <iostream>
int main() {
    for (int i = 0; i > -1; i++) {
        std::cout << i << std::endl;
        std::this_thread::sleep_for(std::chrono::seconds(1));
    }
    return 0;
}