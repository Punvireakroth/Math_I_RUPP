#include<iostream>

void JacobiMethod(int n)
{
	std::cout << "Jacobi's Method" << std::endl;
	float x=0, y = 0;
	float temp_x = 0;
	for (int i = 0; i < n; i++)
	{
		temp_x = -1.0f / 2 * y + 2;
		y = 1.0f / 3 * x + 5.0f / 3;
		x = temp_x;

		std::cout << i+1 <<". x:" << x << "\ty: " << y << std::endl;
	}
	
}



int main()
{
	std::cout << "Please input the number of iteration for Jacobi's method: ";
	int n;
	std::cin >> n;
	JacobiMethod(n);
	
}