#include <math.h>  
#include <opencv2/opencv.hpp>  
  
using namespace std;  
using namespace cv;  
  
const double PI = 3.14159265358979323846;  
const int g_N = 7;  
  
Mat M00 = (Mat_<double>(7, 7) <<  
    0, 0.0287, 0.0686, 0.0807, 0.0686, 0.0287, 0,  
    0.0287, 0.0815, 0.0816, 0.0816, 0.0816, 0.0815, 0.0287,  
    0.0686, 0.0816, 0.0816, 0.0816, 0.0816, 0.0816, 0.0686,  
    0.0807, 0.0816, 0.0816, 0.0816, 0.0816, 0.0816, 0.0807,  
    0.0686, 0.0816, 0.0816, 0.0816, 0.0816, 0.0816, 0.0686,  
    0.0287, 0.0815, 0.0816, 0.0816, 0.0816, 0.0815, 0.0287,  
    0, 0.0287, 0.0686, 0.0807, 0.0686, 0.0287, 0);  
  
Mat M11R = (Mat_<double>(7, 7) <<  
    0, -0.015, -0.019, 0, 0.019, 0.015, 0,  
    -0.0224, -0.0466, -0.0233, 0, 0.0233, 0.0466, 0.0224,  
    -0.0573, -0.0466, -0.0233, 0, 0.0233, 0.0466, 0.0573,  
    -0.069, -0.0466, -0.0233, 0, 0.0233, 0.0466, 0.069,  
    -0.0573, -0.0466, -0.0233, 0, 0.0233, 0.0466, 0.0573,  
    -0.0224, -0.0466, -0.0233, 0, 0.0233, 0.0466, 0.0224,  
    0, -0.015, -0.019, 0, 0.019, 0.015, 0);  
  
Mat M11I = (Mat_<double>(7, 7) <<  
    0, -0.0224, -0.0573, -0.069, -0.0573, -0.0224, 0,  
    -0.015, -0.0466, -0.0466, -0.0466, -0.0466, -0.0466, -0.015,  
    -0.019, -0.0233, -0.0233, -0.0233, -0.0233, -0.0233, -0.019,  
    0, 0, 0, 0, 0, 0, 0,  
    0.019, 0.0233, 0.0233, 0.0233, 0.0233, 0.0233, 0.019,  
    0.015, 0.0466, 0.0466, 0.0466, 0.0466, 0.0466, 0.015,  
    0, 0.0224, 0.0573, 0.069, 0.0573, 0.0224, 0);  
  
Mat M20 = (Mat_<double>(7, 7) <<  
    0, 0.0225, 0.0394, 0.0396, 0.0394, 0.0225, 0,  
    0.0225, 0.0271, -0.0128, -0.0261, -0.0128, 0.0271, 0.0225,  
    0.0394, -0.0128, -0.0528, -0.0661, -0.0528, -0.0128, 0.0394,  
    0.0396, -0.0261, -0.0661, -0.0794, -0.0661, -0.0261, 0.0396,  
    0.0394, -0.0128, -0.0528, -0.0661, -0.0528, -0.0128, 0.0394,  
    0.0225, 0.0271, -0.0128, -0.0261, -0.0128, 0.0271, 0.0225,  
    0, 0.0225, 0.0394, 0.0396, 0.0394, 0.0225, 0);  
  
Mat M31R = (Mat_<double>(7, 7) <<  
    0, -0.0103, -0.0073, 0, 0.0073, 0.0103, 0,  
    -0.0153, -0.0018, 0.0162, 0, -0.0162, 0.0018, 0.0153,  
    -0.0223, 0.0324, 0.0333, 0, -0.0333, -0.0324, 0.0223,  
    -0.0190, 0.0438, 0.0390, 0, -0.0390, -0.0438, 0.0190,  
    -0.0223, 0.0324, 0.0333, 0, -0.0333, -0.0324, 0.0223,  
    -0.0153, -0.0018, 0.0162, 0, -0.0162, 0.0018, 0.0153,  
    0, -0.0103, -0.0073, 0, 0.0073, 0.0103, 0);  
  
Mat M31I = (Mat_<double>(7, 7) <<  
    0, -0.0153, -0.0223, -0.019, -0.0223, -0.0153, 0,  
    -0.0103, -0.0018, 0.0324, 0.0438, 0.0324, -0.0018, -0.0103,  
    -0.0073, 0.0162, 0.0333, 0.039, 0.0333, 0.0162, -0.0073,  
    0, 0, 0, 0, 0, 0, 0,  
    0.0073, -0.0162, -0.0333, -0.039, -0.0333, -0.0162, 0.0073,  
    0.0103, 0.0018, -0.0324, -0.0438, -0.0324, 0.0018, 0.0103,  
    0, 0.0153, 0.0223, 0.0190, 0.0223, 0.0153, 0);  
  
Mat M40 = (Mat_<double>(7, 7) <<  
    0, 0.013, 0.0056, -0.0018, 0.0056, 0.013, 0,  
    0.0130, -0.0186, -0.0323, -0.0239, -0.0323, -0.0186, 0.0130,  
    0.0056, -0.0323, 0.0125, 0.0406, 0.0125, -0.0323, 0.0056,  
    -0.0018, -0.0239, 0.0406, 0.0751, 0.0406, -0.0239, -0.0018,  
    0.0056, -0.0323, 0.0125, 0.0406, 0.0125, -0.0323, 0.0056,  
    0.0130, -0.0186, -0.0323, -0.0239, -0.0323, -0.0186, 0.0130,  
    0, 0.013, 0.0056, -0.0018, 0.0056, 0.013, 0);  
  
  
  
int main()  
{  
  
    Mat OriginalImage = imread("original.png", 0);  
    Mat SubImage = OriginalImage;  
  
    Mat NewSmoothImage;  
    medianBlur(OriginalImage, NewSmoothImage, 13);  
  
    Mat NewAdaThresImage;  
    adaptiveThreshold(NewSmoothImage, NewAdaThresImage, 255, ADAPTIVE_THRESH_GAUSSIAN_C, THRESH_BINARY_INV, 7, 4);  
  
    vector<Point2d> SubEdgePoints;  
  
    Mat ZerImageM00;  
    filter2D(NewAdaThresImage, ZerImageM00, CV_64F, M00, Point(-1, -1), 0, BORDER_DEFAULT);  
    //////////filter2D( cannyImage, zerImageM00, CV_64F, M00, Point(-1,-1), 0, BORDER_DEFAULT);  
  
    Mat ZerImageM11R;  
    filter2D(NewAdaThresImage, ZerImageM11R, CV_64F, M11R, Point(-1, -1), 0, BORDER_DEFAULT);  
    //////////filter2D( cannyImage, zerImageM11R, CV_64F, M11R, Point(-1, -1), 0, BORDER_DEFAULT);  
  
    Mat ZerImageM11I;  
    filter2D(NewAdaThresImage, ZerImageM11I, CV_64F, M11I, Point(-1, -1), 0, BORDER_DEFAULT);  
    //////////filter2D( cannyImage, zerImageM11I, CV_64F, M11I, Point(-1, -1), 0, BORDER_DEFAULT);  
  
    Mat ZerImageM20;  
    filter2D(NewAdaThresImage, ZerImageM20, CV_64F, M20, Point(-1, -1), 0, BORDER_DEFAULT);  
    //////////filter2D( cannyImage, zerImageM20, CV_64F, M20, Point(-1, -1), 0, BORDER_DEFAULT);  
  
    Mat ZerImageM31R;  
    filter2D(NewAdaThresImage, ZerImageM31R, CV_64F, M31R, Point(-1, -1), 0, BORDER_DEFAULT);  
    //////////filter2D(cannyImage, zerImageM31R, CV_64F, M31R, Point(-1, -1), 0, BORDER_DEFAULT);  
  
    Mat ZerImageM31I;  
    filter2D(NewAdaThresImage, ZerImageM31I, CV_64F, M31I, Point(-1, -1), 0, BORDER_DEFAULT);  
    //////////filter2D(cannyImage, zerImageM31I, CV_64F, M31I, Point(-1, -1), 0, BORDER_DEFAULT);  
  
    Mat ZerImageM40;  
    filter2D(NewAdaThresImage, ZerImageM40, CV_64F, M40, Point(-1, -1), 0, BORDER_DEFAULT);  
    //////////filter2D(cannyImage, zerImageM40, CV_64F, M40, Point(-1, -1), 0, BORDER_DEFAULT);  
  
  
  
    int row_number = NewAdaThresImage.rows;  
    int col_number = NewAdaThresImage.cols;  
    //使用7个的7*7的Zernike模板（其本质是个矩阵）M00、M11R、M11I、M20、M31R、M31I、M40，分别与图像进行卷积，得到每个像素点的七个Zernike矩Z00、Z11R、Z11I、Z20、Z31R、Z31I、Z40  
    //对于每个点，根据它的七个Zernike矩，求得距离参数l和灰度差参数k，当l和k都满足设定的条件时，则判读该点为边缘点，并进一步利用上述7个Zernike矩求出该点的亚像素级坐标  
    //如果l或k不满足设定的条件，则该点不是边缘点，转到下一个点求解距离参数l和灰度差参数k  
    for (int i = 0; i < row_number; i++)  
    {  
        for (int j = 0; j <col_number; j++)  
        {  
            if (ZerImageM00.at<double>(i, j) == 0)  
            {  
                continue;  
            }  
  
            //compute theta  
            //vector<vector<double> > theta2(0);  
            double theta_temporary = atan2(ZerImageM31I.at<double>(i, j), ZerImageM31R.at<double>(i, j));  
            //theta2[i].push_back(thetaTem);  
  
            //compute Z11'/Z31'  
            double rotated_z11 = 0.0;  
            rotated_z11 = sin(theta_temporary)*(ZerImageM11I.at<double>(i, j)) + cos(theta_temporary)*(ZerImageM11R.at<double>(i, j));  
            double rotated_z31 = 0.0;  
            rotated_z31 = sin(theta_temporary)*(ZerImageM31I.at<double>(i, j)) + cos(theta_temporary)*(ZerImageM31R.at<double>(i, j));  
  
            //compute l  
            double l_method1 = sqrt((5 * ZerImageM40.at<double>(i, j) + 3 * ZerImageM20.at<double>(i, j)) / (8 * ZerImageM20.at<double>(i, j)));  
            double l_method2 = sqrt((5 * rotated_z31 + rotated_z11) / (6 * rotated_z11));  
            double l = (l_method1 + l_method2) / 2;  
            //compute k/h  
            double k, h;  
          
            k = 3 * rotated_z11 / 2 / pow((1 - l_method2*l_method2), 1.5);  
            h = (ZerImageM00.at<double>(i, j) - k*PI / 2 + k*asin(l_method2) + k*l_method2*sqrt(1 - l_method2*l_method2)) / PI;  
  
            //judge the edge  
            double k_value = 20.0;  
          
            double l_value = sqrt(2) / g_N;  
          
            double absl = abs(l_method2 - l_method1);  
            if (k >= k_value && absl <= l_value)  
            {  
                Point2d point_temporary;  
                point_temporary.x = j + g_N*l*cos(theta_temporary) / 2;  
                point_temporary.y = i + g_N*l*sin(theta_temporary) / 2;  
                SubEdgePoints.push_back(point_temporary);  
            }  
            else  
            {  
                continue;  
            }  
        }  
    }  
    //显示所检测到的亚像素边缘  
    for (size_t i = 0; i < SubEdgePoints.size(); i++)  
    {  
        Point center_forshow(cvRound(SubEdgePoints[i].x), cvRound(SubEdgePoints[i].y));  
        circle(OriginalImage, center_forshow, 1, Scalar(0, 97, 255), 1, 8, 0);  
    }  
    imshow("亚像素边缘", OriginalImage);  
      
    waitKey(0);  
    return 0;  
}