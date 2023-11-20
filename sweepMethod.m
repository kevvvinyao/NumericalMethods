% input parameters for the SLAEs
n = input("Please input the number of equations: ");
a = zeros(n, 1);
b = zeros(n, 1);
c = zeros(n, 1);
d = zeros(n, 1);
p = zeros(n, 1);
q = zeros(n, 1);
x = zeros(n, 1);

fprintf("The value of a[1] has been set to 0 automatically \n");
for i = 2:n
    a(i) = input(sprintf("Please input the value of a[%d]: ", i));
end

fprintf("All elements of a complete!\n");

for i = 1:n
    b(i) = input(sprintf("Please input the value of b[%d]: ", i));
end

fprintf("All elements of b complete!\n");

fprintf("The value of c[n] has been set to 0 automatically \n");

for i = 1:(n-1)
    c(i) = input(sprintf("Please input the value of c[%d]: ", i));
end

fprintf("All elements of c complete!\n");

for i = 1:n
    d(i) = input(sprintf("Please input the value of d[%d]: ", i));
end

p(1) = -c(1)/b(1);
q(1) = d(1)/b(1);

for i = 2:n
    p(i) = -c(i)/(b(i) + a(i) * p(i - 1));
    q(i) = (d(i) - a(i) * q(i - 1))/(b(i) + a(i) * p(i - 1));
end

deter = 1.0 * b(1);

for i = 2:n
    deter = deter * (b(i) + a(i) * p(i - 1));
end

fprintf("The determinant of matrix is %f \n", deter);

x(n) = q(n);

for i = (n-1):-1:1
    x(i) = p(i) * x(i + 1) + q(i);
end

for i = 1:n 
    fprintf("x[%d] is %f \n", i, x(i));
end

