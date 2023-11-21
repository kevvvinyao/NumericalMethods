#include <stdio.h>
#include <math.h>

int main(){
    double A[5][5]={0},B[5][5]={0}, b[5]={0}, x[5]={0},X[5][5]={0}, det=0, temp=0;
    int i,j,k,z,y,flag=0;
    B[1][1]=1;
    B[2][2]=1;
    B[3][3]=1;
    B[4][4]=1;
    printf("Enter your parameters\n");
    for(i=1;i<5;i++)
    {
        scanf("%lf %lf %lf %lf %lf",&A[i][1],&A[i][2],&A[i][3],&A[i][4],&b[i]);
    }
    for(k=1;k<4;k++)
    {
        for(z=k+1;z<5;z++)
        {
            if (abs(A[k][k])<abs(A[z][k]))
            {
                flag=flag+1;
                temp=b[k];
                b[k]=b[z];
                b[z]=temp;
                for(y=1;y<5;y++)
                {
                    temp=A[k][y];
                    A[k][y]=A[z][y];
                    A[z][y]=temp;
                    temp=B[k][y];
                    B[k][y]=B[z][y];
                    B[z][y]=temp;
                }
            }
        }
        if(A[k][k]==0)
        {
            printf("Rank(A) != 4 ,Solution is not unique or not available.");
            return 0;
        }
        for(i=k+1;i<5;i++)
        {
            temp=A[i][k];
            for(j=1;j<5;j++)
            {
                A[i][j]=A[i][j]-A[k][j]*temp/A[k][k];
                B[i][j]=B[i][j]-B[k][j]*temp/A[k][k];
            }
            b[i]=b[i]-b[k]*temp/A[k][k];
        }
    }
    for(k=4;k>1;k--)
    {
        for(i=k-1;i>0;i--)
        {
            b[i]=b[i]-b[k]*A[i][k]/A[k][k];
        }
    }
    for(j=1;j<5;j++)
    {
            X[4][j]=B[4][j]/A[4][4];
            X[3][j]=(B[3][j]-X[4][j]*A[3][4])/A[3][3];
            X[2][j]=(B[2][j]-X[4][j]*A[2][4]-X[3][j]*A[2][3])/A[2][2];
            X[1][j]=(B[1][j]-X[4][j]*A[1][4]-X[3][j]*A[1][3]-X[2][j]*A[1][2])/A[1][1];
    }
    det=pow(-1,flag)*A[1][1]*A[2][2]*A[3][3]*A[4][4];
    for(i=1;i<5;i++)
    {
        x[i]=b[i]/A[i][i];
    }
    printf("The solution is:\nx1=%.2lf;x2=%.2lf;x3=%.2lf;x4=%.2lf;\n", x[1], x[2], x[3], x[4]);
    printf("The determinant: det A = %.2lf\n",det);
    printf("The inverse martix: A^(-1) = \n");
    for(i=1;i<5;i++)
    {
        printf("%.3lf %.3lf %.3lf %.3lf\n",X[i][1],X[i][2],X[i][3],X[i][4]);
    }
    return 0;
}