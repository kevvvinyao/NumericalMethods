% input parameters
n = input("Please input the number of equations: ");
% define coefficient matrix a and right-hand side matrix b
a = zeros(n, n);
b = zeros(n, 1);
x = zeros(n, 1);

% define the unity matrix z for calculating inverse matrix
z = eye(n);

t = 0; % times of swaping rows
inv = zeros(n, n);

for i = 1:n
    for j = 1:n
        a(i, j) = input(sprintf("Please input the value of a[%d][%d]: ", i, j));
    end
end

original_matrix = a;

fprintf("Done! Below is the coefficient matrix: \n");
disp(a);

for i = 1:n
    b(i) = input(sprintf("Please input the value of b[%d]: ", i));
end

fprintf("Done! Below is the right side matrix: \n");
disp(b);

for i = 1:(n-1) % since we need (n-1) steps
    % Following cycle is for pivot element selection
    for j = (i+1):n 
        if abs(a(i, i)) < abs(a(j, i))
        % compare the value of first non-zero elements of two rows
            tmp = a(i, :);
            a(i, :) = a(j, :);
            a(j, :) = tmp;
            % if true, swap two rows, as well as the unity matrix
            tmp = z(i, :);
            z(i, :) = z(j, :);
            z(j, :) = tmp;
            tmp = b(i);
            b(i) = b(j);
            b(j) = tmp;
            % and add 1 to the times of swapping
            t = t + 1;
        end
    end

    if a(i, i) == 0 % check if there 
        fprintf("There is no unique solution or not available!\n");
    end
    % Make sure that there is a valid unique solution

    for j = (i+1):n 
        c = -a(j, i)/a(i, i);
        a(j, :) = a(j, :) + a(i, :) * c;
        b(j) = b(j) + b(i) * c;
        z(j, :) = z(j, :) + z(i, :) * c;
        % fprintf("i = %d, j = %d \n", i, j);
    end
    
end

% Now, we have got a, b, z.

deter = (-1) ^ (t);
for i = 1:n
    deter = deter * a(i, i);
end

fprintf("Determinant of the matrix is: \n %f \n", deter);
% backward path

x(n) = b(n)/a(n, n);

for i = (n-1):-1:1 % reverse order to find x
    c = 0;
    for j = (i+1):n 
        c = c + x(j) * a(i, j);
    end
    x(i) = (b(i) - c)/a(i, i);
end

fprintf("The solution: \n");
disp(x);

for i = 1:n % the column index of inv
    inv(n, i) = z(n, i)/a(n, n);
    for j = (n-1):-1:1 % reverse order to find solution
        c = 0;
        for k = (j+1):n 
            c = c + inv(k, i) * a(j, k);
        end
        inv(j, i) = (z(j, i) - c)/a(j, j);
    end
end

fprintf("The inverse matrix: \n");
disp(inv);

% check inverse matrix

check_matrix = original_matrix * inv;
fprintf("The product of inverse and original matrix is: \n");
disp(check_matrix);
