#include <stdio.h>
#include <stdlib.h>

///////////////////////选择法排序
//a：为数组首地址
//n：为数组元素个数
void select_sort(int *a, int n)
{
	int i, j, k, temp;
	for(i = 0; i < n-1; i++)
	{
		k = i;
		for(j = i+1; j < n; j++)
		{
			if(a[k] > a[j])
			{
				k = j;
			}
		}
		
		if(i != k)
		{
			temp = a[i];
			a[i] = a[k];
			a[k] = temp;
		}
	}
}

///////////////////////冒泡法排序
void bubble_sort(int *a, int n)
{
	int i, j, temp;
	for(i = 0; i < n-1; i++)
	{
		for(j = 0; j < n-1-i; j++)
		{
			if(a[j] > a[j+1])
			{
				temp = a[j];
				a[j] = a[j+1];
				a[j+1] = temp;
			}
		}
	}
}

///////////////////////插入法排序
void insert_sort(int *a, int n)
{
	int i, j, temp;
	for(i = 1; i < n; i++)
	{
		temp = a[i];
		for(j = i-1; j >= 0 && a[j] > temp; j--)
		{
			a[j+1] = a[j];//将前面的值往后移
		}
		a[j+1] = temp; //插在a[j]的后面
	}
}

///////////////////////折半排序（希尔排序）
void shell_sort(int *a, int n)
{
	int i, j, flag, temp;
	int gap = n;

	while(gap > 1)
	{
		gap = gap/2; //增量缩小，每次减半(折半)
		do
		{
			flag = 0;
			
			//n-gap是控制上限不让越界
			for(i = 0; i < n-gap; i++)
			{
				j = i + gap; //相邻间隔的前后值进行比较
				if(a[i] > a[j])
				{
					temp = a[i];
					a[i] = a[j];
					a[j] = temp;
					
					flag = 1;
				}
			}
			
		}while(flag != 0);
	}
}

///////////////////////快速排序
//查找位置
int find_pos(int *a, int low, int high)
{
	int val = a[low];
	
	while(low < high)
	{
		while(low < high && a[high] >= val)
		{//大于移动，小于则赋值，降序则相反
			high--;
		}
		a[low] = a[high];
		
		while(low < high && a[low] <= val)
		{//小于移动，大于则赋值，降序则相反
			low++;
		}
		a[high] = a[low];
	}//终止while循环之后low和high一定是相等的
	
	//high可以改为low
	a[low] = val;
	
	return low;
}

//low：第一个元素下标
//high：最后一个元素下标
void quick_sort(int *a, int low, int high)
{
	if(low < high)
	{
		int pos = find_pos(a, low, high);
		quick_sort(a, low, pos-1);
		quick_sort(a, pos+1, high);
	}
}

int main(int argc, char *argv[])
{
	int a[] = {2, 10, 8, 1, 9, 7, 5, 4, 0, 6, 3};
	int n = sizeof(a)/sizeof(a[0]); //数组元素个数
	
	//select_sort(a, n); //选择法排序
	//bubble_sort(a, n); //冒泡法排序
	//insert_sort(a, n); //插入法排序
	//shell_sort(a, n); //折半排序（希尔排序）
	quick_sort(a, 0, n-1); //快速排序
	
	int i = 0;
	for(i = 0; i < n; i++)
	{
		printf("%d ", a[i]);
	}
	printf("\n");
	
	system("pause")
	return 0;
}
