
CREATE TABLE Customers (
    CustomerID INT,
    Name VARCHAR(50),
    City VARCHAR(50),
    Grade INT
);

INSERT INTO Customers VALUES
(1, 'John', 'New York', 120),
(2, 'Sarah', 'Chicago', 90),
(3, 'Mike', 'New York', 80),
(4, 'Anna', 'Boston', 150),
(5, 'David', 'New York', 200);


SELECT * FROM Customers
WHERE City = 'New York'
OR Grade > 100;


SELECT * FROM Customers
WHERE City = 'New York'
AND Grade > 100;