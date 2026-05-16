
CREATE TABLE Employees (
    EmpID INT,
    Name VARCHAR(50),
    Department VARCHAR(50),
    Salary INT
);


INSERT INTO Employees VALUES
(1, 'John', 'Finance', 50000),
(2, 'Sarah', 'HR', 45000),
(3, 'Mike', 'Finance', 60000),
(4, 'Anna', 'IT', 70000);


SELECT * FROM Employees;


SELECT * FROM Employees
WHERE Department = 'Finance';


SELECT * FROM Employees
WHERE Salary > 55000;